months = ['January','February','March','April','May','June',
			'July','August','September','October','November','December']

# print type(months)
monthdict= dict((m[:3].lower(),m) for m in months)
# print dir(short_month)

def valid_month(month):
	short_month = month[:3].lower()
	# print short_month
	if short_month in monthdict.keys():
		return monthdict.get(short_month) # get method retrieves values from dicts


# print valid_month('decdfdf')
## February

def valid_day(day):
	day = int(day)
	if day >= 1 and day <= 31: return day
	else:  return None		

# print valid_day(0)
# print valid_day('1')
# print valid_day(14)
# print valid_day('300')
def valid_year(year):
	year = int(year)
	if year >=1900 and year <= 2020: return year
	else:  return None 

# print valid_year('0')
# print valid_year('1950')
# print valid_year('-11')
# print valid_year('2000')
