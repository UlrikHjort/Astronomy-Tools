########################################################################
#
# Moon_Calculations
#
# Moon_Calculations.py
#
# MAIN
#
# Copyright (C) 1994 Ulrik Hoerlyk Hjort
#
# Moon_Calculations is free software; you can redistribute it
# and/or modify it under terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2,
# or (at your option) any later version.
# Moon_Calculations is distributed in the hope that it will be
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


########################################################################
#
#
#
########################################################################
def moon_position(hours, minutes, seconds, day, month, year):

    d = day_number(hours, minutes, seconds, day, month, year)


    a = 60.2666                                      # mean distance, a.u.
    e = 0.054900                                     # eccentricity)
    M = (115.3654 + 13.0649929509 * d) + (129*360)   # mean anomaly)
    i = 5.1454                                       # Inclination
    N = reduce_angle(125.1228 - 0.0529538083   * d)  # longitude asc. node
    w = reduce_angle(318.0634 + 0.1643573223 * d)    # Arg. of perigee 


    E0 = M + (180.0/pi) * e  * sin(M*pi/180.0) * (1 + e * cos (M*pi/180.0))


    delta = 0.005
    E = 0
    while True:
        E = E0 - (E0 - (180.0/pi) * e * sin(E0*pi/180.0) -M) / (1- e*cos(E0*pi/180.0))

        if abs(E0-E) < delta:
            break
        E0 = E


    # Rectangular coordinates:
    x = a * (cos(E*pi/180.0) -e)
    y = a * sqrt(1- (e **2)) * sin(E*pi/180.0)

                 
    # Distance and true anonaly:
    r = sqrt((x **2) + (y ** 2))
    v = reduce_angle(atan2(y,x) *180.0/pi)



    # Ecliptic coordinates:
    x_eclip = r * (cos(N*pi/180.0) * cos ((v+w) * pi/180.0) - sin(N*pi/180.0) * sin((v+w) * pi/180.0) * cos(i*pi/180.0))
    y_eclip = r * (sin(N*pi/180.0) * cos ((v+w) * pi/180.0) + cos(N*pi/180.0) * sin((v+w) * pi/180.0) * cos(i*pi/180.0))
    z_eclip = r * sin((v+w) * pi/180.0) * sin(i*pi/180.0)


    # Ecliptic latitude, longitude, distance:

    lat= asin((z_eclip/r) )  * 180.0 / pi
    lon = reduce_angle(atan2(y_eclip,x_eclip) * 180.0 /pi)


    return (lat,lon,r)
    
    

########################################################################
#
#
#
########################################################################
def moon_position_high_accuracy(hours, minutes, seconds, day, month, year):
    None
