class Student:
    #share variable 
    school_name = "KIT"
    school_location = "Kampong Speu"

    counter = 0
    def __init__(self): #Constructor function, no need to call it 
        Student.counter +=1
        print(Student.counter, "Object created Constructor invoked")

    def display(self): 
        print() #if you want to use share variable you need to call class.varialbe to want to call 

    def __del__(self): #Destructor invokes automatically whenever an object is destroyed
        print("Object destroyed")


    
monirith = Student()
somphors = Student()
rotha = Student()
Rotha = Student()

print("=="*10)

monirith.display()
somphors.display()
rotha.display()
Rotha.display()
#Garbage collector in Python : clean after all the object and variable 

print("=="*10)
#After __init____ we delete it back wit the help of __del__