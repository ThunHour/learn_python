# #Parent class ==> General 
# class Animal:

#     def __init__(self, weight, height, speed, color):

#         self.weight = weight
#         self.height = height
#         self.speed = speed
#         self.color = color

#     def displayAnimal(self):
#         print(self.weight)
#         print(self.height)
#         print(self.speed)
#         print(self.color)
#         print("I am a Animal")

# #Childrean ==> more specific
# class Cat(Animal):

#     def displayCat(self):
#         print(self.weight)
#         print(self.height)
#         print(self.speed)
#         print(self.color)
#         print("I am a cat")
    

# class Lion(Cat):
    
#     def displayLion(self):
#         print(self.weight)
#         print(self.height)
#         print(self.speed)
#         print(self.color)
#         print("I am Lion")
 
# lion = Lion(150,100,25, "Golden Brown") #You can assign anything because Lion is the lowest rank
# lion.displayLion()
# # lion.displayAnimal()  ==> it will take value from Animal class
# # lion.displayCat() ==> it will take values from Cat class 

# print("*"*10)

# cat = Cat(50,50,200,"Black") #You can assign cat and Animal class but not lion 
# cat.displayCat()


# animal = Animal(50,50,50, "Blue")
# animal.displayAnimal() #You cant access cat and lion because Animal is the higest rank  



#other example 

# class Animal:

#     def __init__(self, weight, height, speed, color):
#         self.weight = weight
#         self.height = height
#         self.speed = speed
#         self.color = color

#     def display(self):
#         print(self.weight)
#         print(self.height)
#         print(self.speed)
#         print(self.color)
#         print("I am a Animal")
#         pass

# #Childrean ==> more specific
# class Cat(Animal):

#     #Function overwriting
#     def display(self):
#         print(self.weight)
#         print(self.height)
#         print(self.speed)
#         print(self.color)
#         print("I am a Cat")

# class Lion(Cat):

#     #Function overwriting
#     def display(self):
#         print(self.weight)
#         print(self.height)
#         print(self.speed)
#         print(self.color)
#         print("I am a Lion")
        

# lion = Lion(150,100,25, "Golden Brown") #You can assign anything because Lion is the lowest rank
# lion.display()
# # lion.displayAnimal()  ==> it will take value from Animal class
# # lion.displayCat() ==> it will take values from Cat class 

# print("*"*10)

# cat = Cat(50,50,200,"Black") #You can assign cat and Animal class but not lion 
# cat.display()


# print("*"*10)

# animal = Animal(50,50,50, "Blue")
# animal.display() #You cant access cat and lion because Animal is the higest rank  


#redefinding a function in the subclass that is already created in the parent class
#the function that is created in the subclass will be given more preference as it is considered it is the most specific



#Other example 

class Animal:

    def __init__(self, weight, height, speed, color):
        self.weight = weight
        self.height = height
        self.speed = speed
        self.color = color

    def display(self):
        print(self.weight)
        print(self.height)
        print(self.speed)
        print(self.color)
        print("I am a Animal")
        pass

#Childrean ==> more specific
class Cat(Animal):

    #Function overwriting
    def display(self):
        super().display() # They will call everything in Animal 
        print("I am a Cat")
        print("GG")

class Lion(Cat):

    #Function overwriting
    def display(self):
        super().display() #super use for call parent parameter
        print("I am a Lion") #It will print anything from the top to themselve


lion = Lion(100,200,50,"Golden Brown")
lion.display() #it will print anything from top to botto m


cat = Cat(200,400,10,"Black")
cat.display()
