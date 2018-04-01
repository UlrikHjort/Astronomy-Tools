########################################################################
#
# Orbital_Elements
#
# Orbital_Elements.py
#
# MAIN
#
# Copyright (C) 1994 Ulrik Hoerlyk Hjort
#
# Orbital_Elements is free software; you can redistribute it
# and/or modify it under terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2,
# or (at your option) any later version.
# Orbital_Elements is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# You should have received a copy of the GNU General
# Public License distributed with Yolk. If not, write to the Free
# Software Foundation, 51 Franklin Street, Fifth Floor, Boston,
# MA 02110 - 1301, USA.
######################################################################## 



def sun(d):
  return {'N': 0.0,
           'i' : 0.0,
           'w' : 282.9404 + (4.70935 * (10 ** -5)) *d ,
           'a' : 1.000000, 
           'e': 0.016709 - (1.151 * (10 ** -9))* d, 
           'M': 356.0470 + 0.9856002585 * d
         }


def object(d):
  return {'N': 0.0,
           'i' : 0.0,
           'w' : 0.0 *d ,
           'a' : 0.000000, 
           'e': 0.0 * d, 
           'M': 0.0 * d
         }

    
    



