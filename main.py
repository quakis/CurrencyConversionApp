
import conversions

def askInput():
	current = input("\n\nPlease enter the current ISO of Currency or Cryptocurrency\n").upper().strip()
	amount = float(input("Please enter the dollar or crypto amount\n").strip().replace("$", "").replace(",", ""))
	target = input("Please enter the ISO of Currency or Cryptocurrency you would like to convert to\n").upper().strip()
	return current, target, amount

def test():
	data = conversions.convert("USD", "NZD", 1)
	print("\nThis converts $1 NZD to USD which is " + str(data))
	data = conversions.convert("BTC", "ETH", 1)
	print("\nThis converts 1 BTC to ETH which is " + str(data))
	data = conversions.convert("NZD", "BTC", 100000)
	print("\nThis converts $100,000 NZD to BTC which is " + str(data))
	data = conversions.convert("BTC", "NZD", 1)
	print("\nThis converts 1 BTC to NZD which is " + str(data))

def solution():
	current, target, amount = askInput()
	data = conversions.convert(current, target, amount)
	return data

print(solution())