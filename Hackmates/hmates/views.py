from django.shortcuts import render
#from django.http import HttpResponse
import json, datetime
from urllib.request import urlopen, Request



# Create your views here.
def index(request):
	context_dict = { 'boldmessage':'Is it bold? TEST'}
	return render(request, 'hmates/indexpage.html', context_dict)

#get upcoming hacks list
def Up_list(query):
	year = query[0]
	month = query[1]
	url = 'http://www.hackalist.org/api/1.0/2016/03.json'
	req = Request(url, headers={'User-Agent' : "Magic Browser"})
	json_obj = urlopen(req).read()
	data = json.loads(json_obj.decode('utf-8'))
	return data


def Upcoming_hacks(request):
	month = '03'
	year = '2016'
	hackathon_details = []
	all_data = Up_list([year,month])
	if month == '01':
	    month_word = 'January'
	elif month == '02':
	    month_word = 'February'
	elif month == '03':
	    month_word = 'March'
	elif month == '04':
	    month_word = 'April'
	elif month == '05':
	    month_word = 'May'
	elif month == '06':
	    month_word = 'June'
	elif month == '07':
	    month_word = 'July'
	elif month == '08':
	    month_word = 'August'
	elif month == '09':
	    month_word = 'September'
	elif month == '10':
	    month_word = 'October'
	elif month == '11':
	    month_word = 'November'
	elif month == '12':
	    month_word = 'December'
	hackathon_details = all_data[month_word]
	for particular_hacks in hackathon_details:
		s_date = particular_hacks['startDate']
		e_date = particular_hacks['endDate']
		if s_date.split()[0] == 'December' and e_date.split()[0] =='January':  #split into list and get the first word
			s_year = particular_hacks['year']
			e_year = str(int(particular_hacks['year']) + 1)
		else:
			s_year = particular_hacks['year']
			e_year = s_year
		full_startdate = s_date + ' ' + s_year
		full_enddate = e_date + ' ' + e_year
		particular_hacks['startDate'] = datetime.datetime.strptime( full_startdate, '%B %d %Y')
		particular_hacks['endDate'] = datetime.datetime.strptime( full_enddate, '%B %d %Y')

	return render(request, 'hmates/upcoming.html', {'hackathon_details' : hackathon_details, 'today': datetime.datetime.today().date()})   #must send as a dictionary
