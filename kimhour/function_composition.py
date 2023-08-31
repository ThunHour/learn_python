
#Parent
def grading(total_mark):

    if total_mark > 85:
        return "A"
    elif total_mark > 50:
        return "B"
    else:
        return "F"
    
#childrean
def findTotal(marks):

    return sum(marks)

lists_of_mark = [15,20,12,3]
print(grading(findTotal(lists_of_mark)))

