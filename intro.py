class employee():
    section = 'A'
    def __init__(self,name,age,id,salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id
    
emp1 = employee("harshit",22,6786,45678)
print(emp1.__dict__)
print(employee.section)
print(emp1.section)