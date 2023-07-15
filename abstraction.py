class animal():
    # concrete method
    def eat(self):
        print("the animal eats")
    # abstract method
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        print("and barks")
class snake(animal):
    def sound(self):
        print("hiss")
        
obj = dog()
obj.eat()
obj.sound()