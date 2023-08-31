class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SlList:
    def __init__(self):
        self.head = None
    def Display(self):
        position=self.head
        while position is not None:
            print(position.data)
            position=position.next

linkedlist = SlList()
linkedlist.Head = Node("100")
num1 = Node("200")
num2 = Node("300")
num3 = Node("400")
num4 = Node("500")
linkedlist.Head.next = num1
num1.next = num2
num2.next = num3
num3.next = num4
linkedlist.Display()
