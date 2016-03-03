
points = [(40.7128, -74.0059), (None, None), (40.7128, -74.0059), (26.876, -82.2681)]
def gmaps_img(points):
    GMAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?size=380x263&sensor=false"
    for lat, lon in points:
    	GMAPS_URL += '&markers=%s,%s' % (lat, lon)
    return GMAPS_URL


# print gmaps_img(points)

def gmaps_street(string1,string2):
    street_map = "https://maps.googleapis.com/maps/api/streetview?size=600x300&location=%s,%s&sensor=false" % (string1, string2)
    return street_map

print gmaps_street("2400 Atlantic Ave", "Waukegan")