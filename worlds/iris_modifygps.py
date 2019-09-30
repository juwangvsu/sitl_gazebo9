#!/usr/bin/env python
#Ju Wang, Virginia State Univ
#10/28/2018 
import sys
sys.stderr.write(str(sys.argv))
if (len(sys.argv))<5:
	sys.stderr.write('usage: python $@ xx yy zz srcfile. where xx is gps_lat, yy is gps_lon, zz is gps_alt, lat and lon in radian format')
#filepath = 'iris_px4_standoff_demo_cam1/model.sdf'
filepath = sys.argv[4]
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
 #      print("Line {}: {}".format(cnt, line.strip()))
	fields = line.split(':')

	if line.find('gps_lat')>0:
		print(' <gps_lat>'+str(sys.argv[1]) + '</gps_lat>')
	elif line.find('gps_lon')>0:
		print(' <gps_lon>' +str(sys.argv[2])+ '</gps_lon>')
	elif line.find('gps_alt')>0:
		print(' <gps_alt>' +str(sys.argv[3])+ '</gps_alt>')
	else:
		print(line),	

        line = fp.readline()
        cnt += 1
