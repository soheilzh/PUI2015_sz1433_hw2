import json
import sys
import csv

if __name__=='__main__':
    url = 'https://api.prod.obanyc.com/api/siri/vehicle-monitoring.jason?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1]) % (sys.argv[2])
    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())
    
    jsonFile = open(sys.argv[1], 'r')
    data = json.load(jsonFile)
    stations = data['stationBeanList']

    with open(sys.argv[2], 'w') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Station Name', 'Latitude', 'Longitude']
        writer.writerow(headers)

        for s in stations:
            if s['statusKey']!=1 and s['stationName'].startswith('Coming soon'):
                stationName = s['stationName'][13:]
                stationLat  = s['latitude']
                stationLon  = s['longitude']
                
                writer.writerow([stationName, stationLat, stationLon])
