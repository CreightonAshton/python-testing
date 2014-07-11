num_stocks = int(input("How many stocks do you want to track? "))
my_portfolio = {}

for i in range(num_stocks):
	my_stock_name = str(input("Name of stock: ")).upper()
	my_stock_price = float(input("Current value of " + my_stock_name + ": "))
	my_portfolio[my_stock_name] = my_stock_price

folio = open("portfolios\my_portfolio.txt", "r+")
for stock, price in my_portfolio.items():
	string_to_write = str(stock) + ": " + str(price) + "\n"
	folio.write(string_to_write)
folio.close()