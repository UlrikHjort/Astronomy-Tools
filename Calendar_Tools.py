########################################################################
#
# Calendar_Tools
#
# Calendar_Tools.py
#
# MAIN
#
# Copyright (C) 1994 Ulrik Hoerlyk Hjort
#
# Calendar_Tools is free software; you can redistribute it
# and/or modify it under terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2,
# or (at your option) any later version.
# Calendar_Tools is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# You should have received a copy of the GNU General
# Public License distributed with Yolk. If not, write to the Free
# Software Foundation, 51 Franklin Street, Fifth Floor, Boston,
# MA 02110 - 1301, USA.
######################################################################## 

######################################################################
#
# Convert Julian day o Gregorian date
#
######################################################################
def julian_day_to_gregorian_date(jd):
    l = jd + 68569
    n = (4*l) / 146097
    l = l - (146097 * n + 3) / 4
    i = (4000 * (l+1)) / 1461001
    l = l - (1461 * i) / 4 + 31
    j = (80 * l) / 2447
    d = l - (2447 * j) / 80
    l = j / 11
    m = j + 2 - ( 12 * l)
    y = 100 * (n-49) + i + l

    return (int(d), int (m), int(y))

######################################################################
#
# Calculate julian day from day, month, year with calendar Julian == "J",
# Gregorian == "G"
#
######################################################################
def julian_day_number(day, month, year, calendar):
    a = (14-month) / 12
    y = year + 4800 -a
    m = month + (12 * a) -3

    if calendar == "J":
        return (day + ((153 * m + 2) / 5) + (365*y) + (y/4) - (y/100) + (y/ 400) - 32045)
    elif calendar == "G":
        return (day + ((153 * m + 2) / 5) + (365*y) + (y/4) - 32083)


######################################################################
#
# Calculate julian day number from day, month, year
#
######################################################################
def julian_day_number1(day, month, year):
    return (1461 * ( year + 4800 + ( month - 14) / 12 )) / 4 + ( 367 * ( month - 2 - 12 * (( month - 14 ) / 12))) / 12 - (3* (( year + 4900 + ( month - 14) / 12) / 100 )) / 4 + day - 32075


######################################################################
#
# Calculate modified julian day number from day, month, year
#
######################################################################
def modified_julian_day_number(day, month, year):
        return julian_day_number(day, month, year, "G") - 2400000.5 

    
######################################################################
#
# Calculate Julian date from hours, minutes, seconds, day, month, year
# and calendar Julian == "J", Gregorian == "G"
#
######################################################################
def julian_date(hours, minutes, seconds, day, month, year, calendar="J"):
    return (julian_day_number(day, month, year, calendar) + ((hours - 12)/24) + (minutes/1440) + (seconds/86440))


######################################################################
#
# Calculate week day from day, month, year
# and calendar Julian == "J", Gregorian == "G"
#
######################################################################
def week_day(day, month, year, calendar):
    day_list = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    jdn = julian_day_number(day, month, year, calendar)
    wd = 1 + ((jdn + 1) % 7)
    
    return day_list[wd-1]
              

######################################################################
#
# Calculate day number from hours, minutes, seconds, day, month, year
#
######################################################################
def day_number(hours, minutes, seconds, day, month, year):
    return int(julian_date(0,0,0,19,4,1990) - 2451543.5)

