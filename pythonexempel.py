class Product:
		price = 0
		count = 0
		tax = 1
		def __init__(self, price, count, tax):
			self.price = price
			self.count = count
			self.tax = tax
		def price_with_tax(self):
			return self.price * self.count * self.tax
		
robot = Product(price= 900, count= 2, tax= 1.25)
book = Product(price= 100, count= 1, tax= 1.06)
husvagn = Product(price= 1000, count=1, tax= 1.25)
print(robot.price_with_tax() + book.price_with_tax() + husvagn.price_with_tax())


