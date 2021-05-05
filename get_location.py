
import socket
from simple_geoip import GeoIP
from get_api_number import get_api

def get_IP():
	host = socket.gethostname()
	port=0
	result = socket.getaddrinfo(host, port, socket.AF_INET6)
	return result[1][4][0]
	

def get_location():
	IP = get_IP()
	api = get_api("location")
	geoip = GeoIP(api)
	data = geoip.lookup(IP)
	return data['location']['city']

	

if __name__ == '__main__':
	
	print(get_location())


