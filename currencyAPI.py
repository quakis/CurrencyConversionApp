import requests

api = "9635ae62e49c5d56d2af17f43b05e3ff"
website = 'http://data.fixer.io/api/latest?access_key=' + api + '&format=1'


def getCurrencyRate(currency):
	response = requests.get(website)
	if response.status_code == 200:
		try:
			data = response.json()["rates"][currency]
			return data
		except:
			return("An error has occured...")

	else:
		return("Api couldn't be reached...\n")

def getCurrencyDict():	
	response = requests.get(website)
	data = response.json()["rates"].keys()
	return data
