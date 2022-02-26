import cryptoAPI
import currencyAPI

class Cryptocurrency():
	def __init__(this, ISO):
		this.ISO = ISO

	def getName(this):
		data = cryptoAPI.getCryptoName(this.ISO)
		return data

	def getPrice(this):
		data = cryptoAPI.getCryptoPrice(this.ISO)
		return data


class Currency():
	def __init__(this, ISO):
		this.ISO = ISO

	def getRate(this):
		data = currencyAPI.getCurrencyRate(this.ISO)
		return data


def getCurrencies():
	dict = {}
	for i in currencyAPI.getCurrencyDict():
		dict[i] = Currency(i)
	return dict

def getCryptocurrencies():
	dict = {}
	for i in cryptoAPI.getCryptocurrencyDict():
		dict[i] = Cryptocurrency(i)
	return dict