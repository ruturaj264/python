class Employee:

    company = 'TCS'

    def __init__(self, name):
        self.name = name


e1 = Employee('ruturaj')

print(e1.company)
print(e1.name)

Employee.company = 'Infosys'
print(e1.company)
print(e1.name)
