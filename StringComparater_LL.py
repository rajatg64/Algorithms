__author__ = 'RAJAT'
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def Print(self):
        temp = self.head

        while(temp):
            print(temp.data)
            temp=temp.next

def Compare(llist, llist1):

    llist = llist.head
    llist1 = llist1.head


    while(llist and llist1 and llist.data == llist1.data):
        llist = llist.next
        llist1 = llist1.next

    if llist and llist1:
        return 1 if llist.data > llist1.data else -1
    if llist and not llist1:
        return 1
    if llist1 and not llist:
        return -1
    return 0

llist = LinkedList()
first = Node('a')
llist.head=first
second = Node('b')
third = Node('c')
first.next = second
second.next = third

llist1 = LinkedList()
first = Node('a')
llist1.head=first
second = Node('b')
third = Node('d')
first.next = second
second.next = third


print(Compare(llist,llist1))

