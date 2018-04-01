from Sun_Calculations import *
from Moon_Calculations import *

print "Sun Position", sun_position(10,0,0,19,4,2009)

RA_Decl = sun_right_ascension_and_declination(10,0,0,19,4,2009)

print "RA_Decl", RA_Decl

print "RA: ",hms_to_str( degress_to_hms(RA_Decl[0]))
print "Decl: ",dms_to_str(degress_to_dms(RA_Decl[1]))

sid_time =  sidereal_time_and_hour_angle(10,0,0,19,4,2009,15.0)

print "Sid time: ",sid_time

print "Sid time:", dms_to_str(degress_to_dms(sid_time))

print "Altitude, Azimuth:", altitude_azimuth(10,0,0,19,4,2009,60.0,15.0)

print "Horizon altitude:",horizon_altitude(10,00,0,19,4,2009,1,55.0,13.0)

print "Moon position: ", moon_position(0,0,0,19,4,1990)


local_noon(12.9801)
