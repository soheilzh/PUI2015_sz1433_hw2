import sys, json, urllib2

key     = sys.argv[1]
num     = sys.argv[2]
outFile = sys.argv[3]

url     = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key={}&VehicleMonitoringDetailLevel=calls&LineRef={}'.format(key, num)
 
response = urllib2.urlopen(url)
info     = json.load( response )
buses    = info['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

with open(outFile, 'w') as f:
    f.write('Latitude,Longitude,Stop Name,Stop Status\n')

    for i in range(len(buses)):
        bus  = buses[i]
        stop = bus['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
        stat = bus['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
        lon  = bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        lat  = bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        
        f.write( (','.join( map(str, [lat, lon, stop, stat])) + '\n') )
    
