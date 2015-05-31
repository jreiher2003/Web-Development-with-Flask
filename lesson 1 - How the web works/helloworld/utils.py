months = ['January','February','March','April','May','June',
			'July','August','September','October','November','December']

# print type(months)
monthdict= dict((m[:3].lower(),m) for m in months)
# print dir(short_month)

def valid_month(month):
	
	short_month = month[:3].lower()
	if short_month in monthdict.keys():
		return monthdict.get(short_month) # get method retrieves values from dicts


print valid_month('decdfdf')
## February