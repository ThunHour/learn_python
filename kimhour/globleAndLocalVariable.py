student_from = "KIT" #Globle variable

def grading():
    name = "Monirith"
    grade = "C"
    age = 25
    # global student_from (To change globle variable from KIT to UP)
    student_from = "UP"
    print(name)
    print(grade)
    print(age)
    print(student_from)  # It will change to UP because global student_from has changed to UP


# def internship():
#    sid = 1234
#    project = "KIT Shuttlebus booking system"

#    print(sid)
#    print(project)
#    print(name) # You cant call name because name is local variable 


# grading()
# internship()
print(student_from) #It will show KIT because it is Globle variable 
grading() # It will change to UP because global student_from has changed to UP
