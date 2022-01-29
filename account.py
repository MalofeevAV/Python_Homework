from transaction import Transaction


class Account(Transaction):
	
	counter = 0
	def __init__(self, account_title="Default", transaction_list=[]):
		Account.counter += 1
		self.__account_number = Account.counter
		self.__account_title = account_title
		self.__transaction_list = transaction_list
		
	@property
	# Номер счета должен быть реализован в виде свойства, доступного только для чтения.
	def account_number(self):
		return self.__account_number

	@property
	# # Название счета должно быть реализовано в виде свойства, доступного для чтения
	def account_title(self):
		return self.__account_title

	@account_title.setter
	# и для записи с проверкой длины названия, которое должно содержать не менее четырех символов.
	def account_title(self, account_title):
		if len(account_title) >= 4:
			self.__account_title = account_title

	def __len__(self):
		# Класс должен поддерживать встроенную функцию len() (возвращая число транзакций)
		return len(self.__transaction_list)

	@property
	def balance(self):
		# balance - возвращающее баланс счета в долларах США
		balance = 0
		for trans in self.__transaction_list:
			balance += trans.usd
		return balance
	
	@property
	def all_usd(self):
		# all_usd - возвращающее True, если все транзакции выполнялись в долларах США, или False — в противном случае.
		for trans in self.__transaction_list:
			if trans.currency != "USD":
				return False
		return True
	


if __name__ == '__main__':
	t1 = Transaction(75000, "17/12/2021", "RUB", usd_conversion_rate=0.014)
	t2 = Transaction(100000, "20/12/2021")
	t3 = Transaction(1500, "18/12/2021", "EUR", usd_conversion_rate=1.13)
	t4 = Transaction(100, "20/12/2021")
	a1 = Account(account_title="New_account_a1", transaction_list=[t1, t2])
	a2 = Account(transaction_list=[t3, t4])
	a3 = Account()
	a3.account_title = "ABC"


	print(a1.account_number, a1.account_title, len(a1), a1.balance, a1.all_usd)
	print(a2.account_number, a2.account_title, len(a2), a2.balance, a2.all_usd)
	print(a3.account_number, a3.account_title, len(a3), a3.balance, a3.all_usd)