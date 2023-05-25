import urllib.request, urllib.parse, urllib.error
import json

serviceURL = 'https://py4e-data.dr-chuck.net/json?address=Ann+Arbor%2C+MI&key=42'  #http://maps.googleapis.com/maps/api/geocode/json?
 
while True:
    address = input('Ingresa una localización: ')
    if len(address) < 1: break
    
    url = serviceURL + urllib.parse.urlencode({'calle': address})
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try: 
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js ['status'] != 'OK':
        print('===== Failure To Retrieve =====')
        print(data)
        continue
    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]

    print('lat', lat, 'lng', lng)
    location = js["results"][0]["formatted_address"]
    print(location)