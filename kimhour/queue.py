# Implement Queue using List(Functions)
q = []
size = int(input("Enter the size of Queue:"))


def Enqueue():
    if len(q) == size:  # check wether the stack is full or not
        print("Queue is Full!!!!")
    else:
        element = input("Enter the element:")
        q.append(element)
        print(element, "is added to the Queue!")


def dequeue():
    if not q:  # or if len(stack)==0
        print("Queue is Empty!!!")
    else:
        e = q.pop(0)
        print("element removed!!:", e)

def removeAll():
    for i in range(len(q)):
        q.pop(0)
def display():
    print(q)
    while True:
        print("Select the Operation:1.Add 2.Delete 3. Display 4. ResetQueue 5. Quit")
        choice = int(input())
        if choice == 1:
            Enqueue()
        elif choice == 2:
            dequeue()
        elif choice == 3:
            display()
        elif choice == 4:
            removeAll()
        elif choice == 5:
            break
        else:
            print("Invalid Option!!!")

display()
