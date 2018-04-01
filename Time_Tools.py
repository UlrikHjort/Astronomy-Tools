########################################################################
#
# Time_Tools
#
# Time_Tools.py
#
# MAIN
#
# Copyright (C) 1994 Ulrik Hoerlyk Hjort
#
# Time_Tools is free software; you can redistribute it
# and/or modify it under terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2,
# or (at your option) any later version.
# Time_Tools is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# You should have received a copy of the GNU General
# Public License distributed with Yolk. If not, write to the Free
# Software Foundation, 51 Franklin Street, Fifth Floor, Boston,
# MA 02110 - 1301, USA.
######################################################################## 

########################################################################
#
#
#
########################################################################
def hms_to_decimal_time(hours, minutes, seconds):
    s = seconds / 60.0
    m = (minutes + s) / 60.0
    return (hours + m)


########################################################################
#
#
#
########################################################################
def decimal_time_to_hms(t):
    h,f = divmod(t,1)
    m,f = divmod(f*60,1)
    s,f= divmod(f*60,1)
    
    return (h,m,s)


########################################################################
#
#
#
########################################################################
def hms_to_UTC(hours, minutes, seconds, zone):
    return ((hours - zone), minutes, seconds)


########################################################################
#
#
#
########################################################################
def decimal_time_to_UTC(t, zone):
    return t - zone

