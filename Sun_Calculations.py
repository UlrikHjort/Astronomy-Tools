########################################################################
#
# Sun_Calculations
#
# Sun_Calculations.py
#
# MAIN
#
# Copyright (C) 1994 Ulrik Hoerlyk Hjort
#
# Sun_Calculations is free software; you can redistribute it
# and/or modify it under terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2,
# or (at your option) any later version.
# Sun_Calculations is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# You should have received a copy of the GNU General
# Public License distributed with Yolk. If not, write to the Free
# Software Foundation, 51 Franklin Street, Fifth Floor, Boston,
# MA 02110 - 1301, USA.
######################################################################## 
from math import *
from Calendar_Tools import *
from Conversion_Tools import *
from Time_Tools import *
import Orbital_Elements

############################################################################
#
#                    S U N
#
############################################################################


######################################################################
#
# Calculate Sun position from hours, minutes, seconds, day, month, year
#
######################################################################
def sun_position(hours, minutes, seconds, day, month, year):

    d = day_number(hours, minutes, seconds, day, month, year)


    orbital_elements =  Orbital_Elements.sun(d)
    w = orbital_elements['w']
    a = orbital_elements['a']
    e = orbital_elements['e']
    M = orbital_elements['M']


    obliquity_of_ecliptic = 23.4393 - 3.563 * (10 ** -7) * d  # Obliquity of the ecliptic



    L = reduce_angle(w + M)  #mean longitude


    # Auxiliary angle and eccentric anomaly:
    E = M + (180.0/pi) * e * sin(M*pi/180.0) * (1 + e * cos(M*pi/180.0))

    # Rectangular coordinates in plane o ecliptic. x-axis points towards perihelion:
    x = cos(E*pi/180.0) -e
    y = sin(E*pi/180.0) * sqrt(1- e ** 2)

    # Distance and true anomaly:
    r = sqrt(x**2 + y**2)
    v = atan2(y,x) * 180.0 / pi

    longitude = v + w

    return (r,reduce_angle(longitude),obliquity_of_ecliptic)

######################################################################
#
# Calculate Sun right ascension and declination from 
# hours, minutes, seconds, day, month, year
#
######################################################################
def sun_right_ascension_and_declination(hours, minutes, seconds, day, month, year):
    r_lon_oblecl = sun_position(hours, minutes, seconds, day, month, year)

    r = r_lon_oblecl[0]
    lon = r_lon_oblecl[1]
    obl_ecl = r_lon_oblecl[2]

    x = r * cos(lon*pi/180.0)
    y = r * sin(lon*pi/180.0)
    z = 0.0

    x_eq = x 
    y_eq = y * cos(obl_ecl*pi/180.0) - z * sin(obl_ecl*pi/180.0)
    z_eq = y * sin(obl_ecl*pi/180.0) + z * cos(obl_ecl*pi/180.0)



    RA = atan2(y_eq,x_eq) * 180.0 /pi
    Decl = asin(z_eq/r)  * 180.0 / pi


    return (RA, Decl)



######################################################################
#
# Calculate sidereal time
#
######################################################################
def sidereal_time_and_hour_angle(hours, minutes, seconds, day, month, year, longitude):
    RA_Decl = sun_right_ascension_and_declination(hours, minutes, seconds, day, month, year)
    
    gmst0 = (RA_Decl[0] + 180.0) / 15.0

    sid_time = gmst0 + hours + (minutes/60.0)  + (seconds / (60.0 ** 2))+ longitude/15.0

    mean_longitude = (RA_Decl[0]/15.0)
    return sid_time


######################################################################
#
#
#
######################################################################
def altitude_azimuth(hours, minutes, seconds, day, month, year, latitude,longitude):
    sid_time =  sidereal_time_and_hour_angle(hours, minutes, seconds, day, month, year, longitude)
    RA_Decl = sun_right_ascension_and_declination(hours, minutes, seconds, day, month, year)
    
    hour_angle = sid_time - RA_Decl[0]/15.0
    
    
    x = cos(hour_angle*15.0*pi/180.0) * cos(RA_Decl[1]*pi/180.0)
    y = sin(hour_angle*15.0*pi/180.0) * cos(RA_Decl[1]*pi/180.0)
    z = sin(RA_Decl[1]*pi/180.0)

    x_h = x * sin(latitude*pi/180.0) -z * cos(latitude*pi/180.0)
    y_h = y
    z_h = x * cos(latitude*pi/180.0) +z * sin(latitude*pi/180.0)

    azimuth = (atan2(y_h,x_h) +pi) * 180.0/pi

    altitude = asin(z_h) *180.0/pi


    return (azimuth, altitude)

######################################################################
#
#
#
######################################################################
def local_noon(longitude):
    standard_meridian = divmod(longitude, 15)[0] +1

    longitude_deviation_time =  (longitude - standard_meridian) / 15.0


######################################################################
#
#
#
######################################################################    
def horizon_altitude(hours, minutes, seconds, day, month, year, zone, lattitude, longitude):

    d = day_number(hours, minutes, seconds, day, month, year)
    orbital_elements =  Orbital_Elements.sun(d)
    w = orbital_elements['w']
    a = orbital_elements['a']
    e = orbital_elements['e']
    M = orbital_elements['M']

    gmst_0 = M + w + 180.0 # Greenwich sidereal time at 00:00 UTC

    UTC = decimal_time_to_UTC(hms_to_decimal_time(hours, minutes, seconds), zone)

    lst = gmst_0 + (UTC*15.0) + longitude   # Local sidereal time

    RA, decl = sun_right_ascension_and_declination(hours, minutes, seconds, day, month, year)


    lha = (lst - RA) * pi/180.0

    return asin(sin((lattitude*pi/180.0)) * sin((decl*pi/180.0)) + cos((lattitude*pi/180.0)) * cos((decl*pi/180.0)) * cos(lha)) #* 180.0/pi

######################################################################
#
#
#
######################################################################
def rise_set(longitude):
    None
