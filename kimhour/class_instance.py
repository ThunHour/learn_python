# class Group:
#     group ='2D'
#
#     def __init__(self,g_id,g_name,g_age):
#       self.g_id=g_id
#       self.g_name=g_name
#       self.g_age=g_age
#     def display( self ):
#         print("Group:" +Group.group)
#         print(f"Id:{self.g_id}")
#         print(f"Name:{self.g_name}")
#         print(f"Age:{self.g_age}")
#
#
#
# kimhour=Group(123, 'Seak kimhour', 19)
# kimhour.display()

class Animal: #Parent/base/Super class
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

class Lion(Animal): #Child/sub/derived
    pass
    

lion_animal = Lion(150, 100, 25, "Golden brow")
lion_animal.display()

class Animal:
    def __init__(self, weight, height, speed, color):
        self.weight = weight
        self.height = height
        self.speed = speed
        self.color = color

    def displayAnimal(self):
        print(self.weight)
        print(self.height)
        print(self.speed)
        print(self.color)
        print("I am an Animal")
class Cat(Animal):
    def displayCat(self):
        print(self.weight)
        print(self.height)
        print(self.speed)
        print(self.color)
        print("I am a Cat")

class Lion(Cat):
    def displayLion(self):
        print(self.weight)
        print(self.height)
        print(self.speed)
        print(self.color)
        print("I am a Lion")
lion = Lion(150,100, 25, "Golden Brown")

lion.displayAnimal()
print("#"*10)
lion.displayCat()
print("#"*10)
lion.displayLion()
