class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkledList:
    def __init__(self):
        self.headval = None

    def listPrint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtLast(self, newData):
        Newdata = Node(newData)

        if self.headval is None:
            self.headval = Newdata
            return
        currentData = self.headval
        while currentData.nextval:
            currentData = currentData.nextval
        currentData.nextval = Newdata


list1 = SLinkledList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.headval.nextval = e2
e2.nextval = e3

list1.AtLast("sun")
list1.listPrint()
