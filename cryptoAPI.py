import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b298a46e-9b42-43b1-87d9-c5973e3cd336',
}
websiteCrypto = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'
websiteCryptocurrencies = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"

	
def getCryptoPrice(crypto):
	try:
		parameters = {
			"amount": "1",
			"symbol": crypto
		}
		session = requests.Session()
		session.headers.update(headers)
		response = session.get(websiteCrypto, params=parameters)
		data = response.json()["data"][0]["quote"]["USD"]["price"]
		return data
	except (ConnectionError, Timeout, TooManyRedirects) as e:
		return(e)

def getCryptoName(crypto):
	try:
		parameters = {
			"amount": "1",
			"symbol": crypto
		}
		session = requests.Session()
		session.headers.update(headers)
		response = session.get(websiteCrypto, params=parameters)
		data = response.json()["data"][0]["name"]
		return data
	except:
		return("An error has occured...")

def getCryptocurrencyDict():
	session = requests.Session()
	session.headers.update(headers)
	response = session.get(websiteCryptocurrencies)
	data = response.json()["data"]
	list = []
	for i in data:
		if i["rank"] <= 100: 
			list.append(i["symbol"])
		else:
			continue
	return sorted(list)







