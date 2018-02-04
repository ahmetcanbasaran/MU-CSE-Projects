class Employee:

	def __init__(self, first, last, pay):

		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullName(self):

		return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Ahmet', 'Alaca' , '50000')
emp_2 = Employee('Mehmet', 'Karaca', '60000')

print(emp_1.first)
print(emp_2.fullName())
