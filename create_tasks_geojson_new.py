#!/bin/python
# -*- coding: iso-8859-15 -*-
#
# Author: B. Herfort, 2015
###########################################

import sys

try:
	input = 'E:/Uni/_Hiwi/osm_nepal/data/idp_camps_with_tags_and_timestamp_center.geojson'
	input_2 = 'E:/Uni/_Hiwi/osm_nepal/data/idp_3857_s.geojson'
	output = 'E:/Uni/_Hiwi/osm_nepal/PyBossa/shelter_dynamics_observer/tasks_shelter_dynamics_observer_new.csv'
except:
    print "ERROR: Not enough program arguments given."
    print "Require %s inputCSV outputCSV" % (sys.argv[0])
    sys.exit(0)

#Open input ascii file for reading
fileobj = file(input,'r')
fileobj_2 = file(input_2,'r')

#Open file for writing
fileobj_output = file(output,'w')

#information about task
app_id = '29'

geom_1 = []
geom_2 = []

#Counter for line number
l=-1
c=0
#Iterate over lines in file
for line in fileobj.readlines():
	print l
	l=l+1
	#if l==0:
	#	o_line = 'id;created;app_id;state;quorum;calibration;priority_0;info;n_answers'+'\n'
	#	fileobj_output.write(o_line)
	if (line.startswith('{ "type": "Feature",') == True):
		lineval = line.strip(',\n').replace('"',"'")
		geom_1.append(lineval)

		
for line_2 in fileobj_2.readlines():
	if (line_2.startswith('{ "type": "Feature",') == True):
		lineval_2 = line_2.strip(',\n').replace('"',"'")
		geom_2.append(lineval_2)
		

for i in range(0, len(geom_1)):
	if i==0:
		o_line = 'id;created;app_id;state;quorum;calibration;priority_0;info;n_answers'+'\n'
		fileobj_output.write(o_line)
	print i
	c=c+1
	task_id = 102000 + c
	lineval = str(geom_1[i])
	lineval_2 = str(geom_2[i])
	o_line = str(task_id)+';;'+app_id+';ongoing;0;0;0;{"GeoJSON_object": "'+lineval+'","GeoJSON_object_trans": "'+lineval_2+'", "id": "'+str(c)+'"};1'+'\n'
	fileobj_output.write(o_line)


fileobj.close()
fileobj_output.close()