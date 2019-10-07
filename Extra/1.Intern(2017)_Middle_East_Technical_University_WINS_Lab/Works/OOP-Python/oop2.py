
class Employee:

	raiseAmount = 1.04
	numberOfEmployees = 0

	def __init__(self, first, last, pay):

		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.numberOfEmployees += 1

	def fullName(self):

		return '{} {}'.format(self.first, self.last)

	def applyIncrease(self):

		self.pay = int(self.pay * 1.04)

print(Employee.numberOfEmployees)
emp_1 = Employee('Ahmet', 'Alaca' , 50000)
print(emp_1.fullName())
print(Employee.numberOfEmployees)
emp_2 = Employee('Mehmet', 'Karaca', 60000)
print(emp_2.fullName())
print(Employee.numberOfEmployees)

print(emp_1.fullName())
print('Before increasing: ' + str(emp_1.pay))

emp_1.applyIncrease()

print('After increasing: ' + str(emp_1.pay))
