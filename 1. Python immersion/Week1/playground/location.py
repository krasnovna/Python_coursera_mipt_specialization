import requests 

def get_location_info():
	r = requests.get("http://api.ipstack.com/2.92.195.199?access_key=5d75a75c32a70e588c2936fda9b0e57b")
	#r.status_code
	return r.json()

if __name__ == "__main__":
	print(get_location_info())
