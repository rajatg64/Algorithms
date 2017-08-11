__author__ = 'RAJAT'
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def AddNode(self,data):
        if  self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while (temp.next):
                temp=temp.next

            temp.next=Node(data)
    def print(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp=temp.next

    def LinkedListSum(self, list1, list2):
        prev = None
        carry = 0
        temp =None
        while  list1 is not None or list2 is not None:
            first = 0 if list1 is None else list1.data
            second = 0 if list2 is None else list2.data
            sum = first + second

            carry = 0 if sum < 10 else 1

            data = sum if carry == 0 else sum%10

            temp = Node(data)

            if  self.head is None:
                self.head = temp
            else:
                prev.next = temp

            prev = temp

            if list1 is not None:
                list1 = list1.next
            if list2 is not None:
                list2 = list2.next

        if carry>0:
            temp.next = Node(carry)

lList = LinkedList()
lList.AddNode(1)
lList.AddNode(2)
lList.AddNode(3)

lList1 = LinkedList()
lList1.AddNode(1)
lList1.AddNode(2)
lList1.AddNode(3)
lList1.AddNode(4)


res = LinkedList()
res.LinkedListSum(lList.head, lList1.head)
res.print()
