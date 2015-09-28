import sys, json, urllib2

if __name__=='__main__':

key = sys.argv[1]
num = sys.argv[2]

url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key={}&VehicleMonitoringDetailLevel=calls&LineRef={}'.format(key, num)

response = urllib2.urlopen(url)
info     = json.load( response )
buses    = info['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print 'Bus Line :', num
print 'Number of Active Buses :', len(buses)
for i in range(len(buses)):
    bus = buses[i]
    lon = bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    lat = bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    print 'Bus {} is at latitude {} and longitude {}'.format(i, lat, lon)
    
