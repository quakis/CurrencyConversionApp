import currencies


def convertCurrency(current, target, amount):
	data = (target.getRate() / current.getRate()) * amount
	return data

def convertCrypto(current, target, amount):
	data = (current.getPrice() / target.getPrice()) * amount
	return data

def convertCurrencyToCrypto(current, target, amount):
	USD = currencies.Currency("USD")
	conversion = convertCurrency(current, USD, 1)
	data = (conversion / target.getPrice()) * amount
	return data

def convertCryptoToCurrency(current, target, amount):
	USD = currencies.Currency("USD")
	conversion = convertCurrency(target, USD, 1)
	data = (current.getPrice() / conversion) * amount
	return data

def convert(current, target, amount):
	if (current in currencyDict) and (target in currencyDict):
		data = convertCurrency(currencyDict[current], currencyDict[target], amount)
		return data
	elif current in cryptocurrencyDict and target in cryptocurrencyDict:
		data = convertCrypto(cryptocurrencyDict[current], cryptocurrencyDict[target], amount)
		return data
	elif current in currencyDict and target in cryptocurrencyDict:
		data = convertCurrencyToCrypto(currencyDict[current], cryptocurrencyDict[target], amount)
		return data
	elif current in cryptocurrencyDict and target in currencyDict:
		data = convertCryptoToCurrency(cryptocurrencyDict[current], currencyDict[target], amount)
		return data
	else:
		return("An error occured...")

currencyDict = currencies.getCurrencies()
cryptocurrencyDict = currencies.getCryptocurrencies()




