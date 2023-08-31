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

if __name__=='__main__':
    list1 = SLinkledList()
    list1.headval = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")
    list1.headval.nextval = e2
    e2.nextval = e3
    list1.listPrint()
