from bs4 import BeautifulSoup
from urllib.request import urlopen

num_stocks = int(input("How many stocks do you want to track? "))
my_portfolio = {}

for i in range(num_stocks):
	my_stock_name = str(input("Name of stock: ")).upper()
	content = urlopen('http://finance.yahoo.com/q?s=' + my_stock_name)
	page_holder = content.read()
	content.close()
	soup = BeautifulSoup(page_holder)
	#print (soup.prettify())
	span_id = 'yfs_184_' + my_stock_name.lower()
	print (span_id)
	print (soup.find_all('span'))
	test = soup.find('yfs_184_')
	print (test)
	#my_stock_price = float(input("Current value of " + my_stock_name + ": "))
	#my_portfolio[my_stock_name] = my_stock_price

folio = open("portfolios\my_portfolio.txt", "r+")
for stock, price in my_portfolio.items():
	string_to_write = str(stock) + ": " + str(price) + "\n"
	folio.write(string_to_write)
folio.close()