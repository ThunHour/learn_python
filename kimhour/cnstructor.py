class Student:
    school_name="KIT"
    school_location="Kampong Speu"
    counter = 0

    def __init__(self): # Constructor are special methods (__init__)(automatic calling)
        Student.counter+=1
        print(Student.counter,"Object Created Constructor invoked")

    def display(self):
        print()

    def __del__(self): # Destructor invokes automatically whenever an object is destroyed
        print("Object destroyed")
monirith = Student()
somphors = Student()
rotha = Student()
kimpor = Student()

print("*"*10)
monirith.display()
somphors.display()
rotha.display()
kimpor.display()
print("*"*10)

#Garbage collector in Python
