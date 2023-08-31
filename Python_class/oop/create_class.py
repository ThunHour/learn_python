#everything in class called blue print
class Car:
    #All of this is attributed

    #class variable 
    #save memory
    color = "White" #common variable 
    num_of_wheel = 4
    max_speed = 150


    #behaviours
    def display_details(self): #self ==> class
        print(Car.color)
        print(Car.num_of_wheel)
        print(Car.max_speed)


#car1, car2 ==> instance (results of blueprint)
car1 = Car() #call function to store in car1
car2 = Car() #call the class to store in car2

car1.display_details()
car2.display_details()

print("=="*10)
#if we change common variable everything will be change base on what you change
Car.color = "Red"
Car.max_speed = 200

car1.display_details()
car2.display_details()