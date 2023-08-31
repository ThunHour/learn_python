class Student:
    # stu_id = 10 #cant create like this because each student has diffrent ID 
    school = "KIT"
    #Instead do this

    #Can create only 1 constructor
    #if no paremater ==> deculat constructor


    #If have parameter ==> paremeterized constructor
    def __init__(self,s_id, s_name, s_age):
        self.s_id = s_id  #self.variable_name => is instant variable , in other language they use "this" instead of "self."
        self.s_name = s_name
        self.s_age = s_age
        print("Object initaialized...")

    
    #instant method ==> method create inside the class and belong to  
    def displayValue(self):
        print(self.s_id)
        print(self.s_name)
        print(self.s_age)
        print(Student.school) #because it is common variable
        return True
    

#if it is share variable, is only take 1 time memory (dont care about how many time you mention it)
#instant variable, is take depend on how many time you assign to the varible


rith = Student(125,"Rith",19) # instant method ==> objec
rith.displayValue()

#
zass = Student(126,"Zass",20)
message = zass.displayValue() #message ==> catch in Python (to catch return)

# print(zass.displayValue())


    

