# class Animal : #Parent/base/super class

#     #You cant inheritance on common variable
#     def __init__(self, weight, height, speed, color):

#         self.weight = weight
#         self.height = height
#         self.speed = speed
#         self.color = color

    
#     def displayValue(self):
#         print(self.weight)
#         print(self.height)
#         print(self.speed)
#         print(self.color)

# #everything in Animal will pass to class Lion
# class Lion(Animal): #Child/sub/dervied
#     pass

# #before having child class
# lion = Animal(150,100,25, "Golden Brown")
# lion.displayValue()

# print("="*10)
# #after having child class
# lion = Lion(150,100,200,"Golden Brown")
# lion.displayValue()





#another example 
class Animal : #Parent/base/super class

    #You cant inheritance on common variable
    def __init__(self, weight, height, speed, color):

        self.weight = weight
        self.height = height
        self.speed = speed
        self.color = color

    
    def displayValue(self):
        print(self.weight)
        print(self.height)
        print(self.speed)
        print(self.color)

#everything in Animal will pass to class Lion
class Lion(Animal): #Child/sub/dervied
    def displayValue(self):
        print(self.weight)
        print(self.height)
        print(self.speed)
        print(self.color)


lion = Lion(100,200,50,"White")
lion = lion.displayValue()

        