# method overloading
# class methods:
#     def __init__(self,a=1,b=1,c=1):
#         self.a = a
#         self.b = b
#         self.c = c
#     def mul(self):
#         return (self.a*self.b)
#     def mul(self):
#         return (self.a*self.b*self.c )
    
# m1 = methods(4,2,3)
# print(m1.mul())      

#method overriding
class methods:
    def showname(self):
        print("aradhya")
    def showage(self):
        print("19")
class overriding(methods):
    def showname(self):
        print("chinu")
        
o1 = methods()
o2 = overriding()
o1.showname()
o2.showname()
o2.showage()