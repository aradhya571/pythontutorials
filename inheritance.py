#single level inheritance
# class employee():
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#     def show1(self):
#         print(self.name ,self.age )

# class childemployee(employee):
#     def show2(self):
#         print(self.salary)
    
# emp1 = childemployee("aradhya",19,2100000)
# emp1.show1()
# emp1.show2()


#multilevel inheritance
# class employee():
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#     def show1(self):
#         print(self.name ,self.age )

# class childemployee1(employee):
#     def __init__(self,name,salary,age):
#         self.salary = salary
#         self.name = name
#         self.age = age
#     def show2(self):
#         print(self.salary)
        
# class childemployee2(childemployee1):
#     def __init__(self,name,salary,age,gender):
#         self.salary = salary
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def show3(self):
#         print(self.gender)
    
# emp1 = employee("papa",50,1900000)
# emp2 = childemployee1("aradhya",21000000,19)
# emp3 = childemployee2("chinu",2100000,19,"F")
# emp3.show1()
# emp3.show2()
# emp3.show3()


#multiple inheritance
class employee1():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def show1(self):
        print(self.name ,self.age )

class employee2():
    def __init__(self,name,salary,age):
        self.salary = salary
        self.name = name
        self.age = age
    def show2(self):
        print(self.salary)
        
class childemployee(employee1,employee2):
    def __init__(self,name,salary,age,gender):
        self.salary = salary
        self.name = name
        self.age = age
        self.gender = gender
    def show3(self):
        print(self.gender)
    
emp3 = childemployee("chinu",2100000,19,"F")
emp3.show1()
emp3.show2()
emp3.show3()







