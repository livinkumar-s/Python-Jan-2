class Bottle:
    # attributes 
    def __init__(self):
        self.radius=40
        self.height=300
        self.color="Black"
        self.name="Aqua Bottles"
    # methods 
    def getVolume(self):
        print("The volume is: "+str((22/7)*(self.radius**2)*self.height))
    
    def open(self):
        print("Bottle is opening...!")


#attributes: 3, method: 2

class Dog(Bottle):
    def __init__(self):
        self.name="Spike"
        self.__age=5
    
    def getAge(self):
        print(self.__age)
    

dog1=Dog()

# print(dog1.__age)
# dog1.getAge()

print(dog1.name)


# bot1=Bottle()
bot2=Bottle()
# bot3=Bottle()
# bot4=Bottle()
# bot5=Bottle()

# print(bot2.radius)
# bot5.getVolume()
# bot4.open()

# a=1
# b="Hello" # str
# c=[1,2,3]

# print(type(bot1)) #<class __main__."Bottle">

# b.upper()
# b.lower()

# a=1
