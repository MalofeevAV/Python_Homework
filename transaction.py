class Transaction():

	def __init__(self, amount, date, currency="USD", usd_conversion_rate=1, description=None):
		self.__amount = amount
		self.__date = date
		self.__currency = currency
		self.__usd_conversion_rate = usd_conversion_rate
		self.__description = description
		

	@property
	def amount(self):
		return self.__amount

	@property
	def date(self):
		return self.__date

	@property
	def currency(self):
		return self.__currency

	@property
	def usd_conversion_rate(self):
		return self.__usd_conversion_rate

	@property
	def description(self):
		return self.__description

	@property
	def usd(self):
		return self.amount*self.usd_conversion_rate


if __name__ == '__main__':
	t1 = Transaction(75000, "17/12/2021", "RUB", usd_conversion_rate=0.014)
	print(t1.amount, t1.date, t1.currency, t1.usd_conversion_rate, t1.description, t1.usd, sep="\n")
