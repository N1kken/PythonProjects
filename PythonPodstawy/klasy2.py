class Cat(object):
    def __init__(self,name):
        self.name=name
class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee,self).__init__(name)
        self.salary = salary

mary = Person("Mary")
satan = Cat("Satan")
mary.pet = satan
frank=Employee("Frank", 120000)
frank.pet = satan

print(frank.name)
print(frank.salary)
print(mary.name)
print(mary.pet)