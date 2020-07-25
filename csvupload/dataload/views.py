from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Project, Facility, Zone
import csv, io, os
from django.contrib import messages

# Create your views here.
def index(request):
	template = "index.html"

	pid = None 
	pname = None
	pdesc = None
	fid = None
	fname = None
	fdesc = None
	zid = None
	zname = None 
	zdesc = None 
	fzid = None
	pfid = None
	
	#form = request.FILES
	if request.method == "POST":

		myfile = request.FILES['file']
		file_name = request.FILES['file'].name

		#checks the file extension
		if not file_name.endswith('.csv'):
			raise ValidationError('Invalid file type')

		pth = os.path.abspath(file_name)
		fn = pth.replace("\\", "/" )

		#stores the csv values
		col_value_project = []
		col_value_facility = []
		col_value_zone = []


		with open(fn, "rt" ) as f:
			data = csv.reader(f)
			row_num = 0
			database_no = 1
			for row in data:
				
				#Reset  row number to read a new table in csv file
				if(row_num == 3):
					row_num = 0
					database_no = database_no + 1
				row_num = row_num+1
				
				for cellvalue in row:
					index_val = 0
					if (cellvalue.find("*") != -1):
						cellvalue=cellvalue[2:]
						print("Database name =  " + cellvalue)
						break;
					elif (cellvalue!= ''):			
						if(row_num == 2):
							pass
							#gets column names
							#print("Column name = " + cellvalue)
						if(row_num == 3):
							if(database_no == 1):
								col_value_project.append(cellvalue)
								#print(col_value_project)
							elif(database_no == 2):
								col_value_facility.append(cellvalue)
								#print(col_value_facility)
							else:
								col_value_zone.append(cellvalue)
								#print(col_value_zone)
					else:
						continue	

		# print(col_value_project)
		# print(col_value_facility)
		# print(col_value_zone)	

		
		pid = col_value_project[0]
		pname = col_value_project[1]
		pdesc = col_value_project[2]

		fid = col_value_facility[0]
		fname = col_value_facility[1]
		fdesc = col_value_facility[2]
		pfid = col_value_facility[3]

		zid = col_value_zone[1]
		zname = col_value_zone[2]
		zdesc = col_value_zone[3]
		fzid = col_value_zone[0]

		#Upload the table values to the backend
		created = Project.objects.create(
			project_id = col_value_project[0],
			project_name = col_value_project[1],
			project_description = col_value_project[2]
		)

		created = Facility.objects.create(
			facility_id = col_value_facility[0],
			facility_name = col_value_facility[1],
			facility_description = col_value_facility[2],
			project_id = col_value_facility[3]
		)

		created = Zone.objects.create(
			facility_id = col_value_zone[0],
			zone_id = col_value_zone[1],
			zone_name = col_value_zone[2],
			zone_description = col_value_zone[3]
		)
		
	return render(request, template, context={'proj_id': pid, 'proj_name': pname, 'proj_desc': pdesc, 
											  'facility_id': fid, 'facility_name': fname, 'facility_desc': fdesc, 'project_facility_id': pfid,
											  'zone_id': zid, 'zone_name': zname, 'zone_desc': zdesc, 'zone_facility_id': fzid})