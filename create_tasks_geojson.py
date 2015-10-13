#!/bin/python
# -*- coding: iso-8859-15 -*-
#
# Author: B. Herfort, 2015
###########################################

import sys

try:
	input = 'E:/Uni/_Hiwi/osm_nepal/data/idp_camps_with_tags_and_timestamp_center.geojson'
	output = 'E:/Uni/_Hiwi/osm_nepal/PyBossa/shelter_dynamics_observer/tasks_shelter_dynamics_observer_geojson.csv'
except:
    print "ERROR: Not enough program arguments given."
    print "Require %s inputCSV outputCSV" % (sys.argv[0])
    sys.exit(0)

#Open input ascii file for reading
fileobj = file(input,'r')

#Open file for writing
fileobj_output = file(output,'w')

#information about task
app_id = '29'



#Counter for line number
l=-1
c=0
#Iterate over lines in file
for line in fileobj.readlines():
	print l
	l=l+1
	lineval = line.strip(',\n').replace('"',"'")
	if l==0:
		o_line = 'id;created;app_id;state;quorum;calibration;priority_0;info;n_answers'+'\n'
		fileobj_output.write(o_line)
	if (line.startswith('{ "type": "Feature",') == True):
		c=c+1
		task_id = 102000 + c
		o_line = str(task_id)+';;'+app_id+';ongoing;0;0;0;{"GeoJSON_object": "'+lineval+'", "id": "'+str(c)+'"};1'+'\n'
		fileobj_output.write(o_line)

fileobj.close()
fileobj_output.close()