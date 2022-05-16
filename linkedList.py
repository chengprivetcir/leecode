class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Method to display the list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next

    # Method to add element to list
    def addToList(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode


listA = LinkedList()
listB = LinkedList()

# Add elements to the list in sorted order
listA.addToList(5)
listA.addToList(10)
listA.addToList(15)

listB.addToList(2)
listB.addToList(3)
listB.addToList(20)
listB.addToList(22)
listB.addToList(24)

def mergeList(la,lb):
    dummy = Node(0)

    tail = dummy

    while la and lb:

        if la.val >= lb.val:
            tail.next = lb
            lb = lb.next
        else:
            tail.next = la
            la = la.next

        tail = tail.next

    if la:
        tail.next=la
    elif lb:
        tail.next = lb

    return dummy.next

#listA.head = mergeList(listA.head,listB.head)


def reverseList(head):
    p1 = None

    while head:
        p3 = head.next
        head.next = p1
        p1= head
        head = p3
    return  p1

listA.head = reverseList(listA.head)


print(listA.printList())
