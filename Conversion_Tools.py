########################################################################
#
# Conversion_Tools
#
# Conversion_Tools.py
#
# MAIN
#
# Copyright (C) 1994 Ulrik Hoerlyk Hjort
#
# Conversion_Tools is free software; you can redistribute it
# and/or modify it under terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2,
# or (at your option) any later version.
# Conversion_Tools is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# You should have received a copy of the GNU General
# Public License distributed with Yolk. If not, write to the Free
# Software Foundation, 51 Franklin Street, Fifth Floor, Boston,
# MA 02110 - 1301, USA.
######################################################################## 
from math import *


######################################################################
#
# Convert degress to hour, minutes, seconds
#
######################################################################
def degress_to_hms(d):
    h = d / 15.0
    m = (h * 60) - int(h) * 60
    s = (m * 60) - int(m) * 60
    return(int(h), int(m), round(s,1))

######################################################################
#
# Convert degress to degress, minutes, seconds
#
######################################################################
def degress_to_dms(d):
    deg = int(d)
    m = (d - deg) * 60
    s = (m - int(m)) * 60

    return (deg, int(m), round(s,1))



######################################################################
#
# Convert Degress Minutes Seconds [N/S/E/W] to decimal degrees
#
######################################################################
def dms_with_suffix_to_decimal_degrees(dms):
    deg = dms[0]
    m = dms[1]
    s = dms[2]
    suffix = dms[3]
   
    suffix_sign = 1
    if suffix == 'S' or suffix == 'W':
        suffix_sign = -1

    return (suffix_sign * (deg + (m/60.0) + (s/60.0/60.0)))


######################################################################
#
# Convert Degress Minutes Seconds to decimal degrees
#
######################################################################
def dms_to_degrees(dms):
    deg = dms[0]
    m = dms[1]
    s = dms[2]
    return deg + (m/60.0) + (s/60.0/60.0)


######################################################################
#
# Convert lat, lon degress to hours, minutes, seconds with N/S/W/E suffix
#
######################################################################
def lat_lon_degrees_to_hms_with_suffix(lat_lon_deg):
    lat_suffix = "N"
    lon_suffix = "E"
    lat = degrees_to_dms(abs(lat_lon_deg[0]))
    lon = degrees_to_dms(abs(lat_lon_deg[1]))

    if lat_lon_deg[0] < 0:
        lat_suffix = "S"        

    if lat_lon_deg[1] < 0:
        lon_suffix = "W"        

    return (lat[0],lat[1],lat[2],lat_suffix), (lon[0],lon[1],lon[2],lon_suffix)




#

######################################################################
#
# hms to hms string
#
######################################################################
def hms_to_str(hms):
    return str(hms[0])+"h" + str(hms[1])+"m" +str(hms[2])+"s"


######################################################################
#
#
#
######################################################################
def dms_to_str(dms):
    return str(dms[0])+"_deg "+ str(dms[1])+"\""+ str(dms[2])+"\'"




######################################################################
#
# Normalize angle
#
######################################################################
def reduce_angle(x):
    return x - floor(x/360.0) * 360.0
