class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=self.head

    def isEmpty(self):
        return self.head==None

    def insertAtHead(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head=newNode
            self.tail=self.head
        else:
            newNode.next=self.head
            self.head=newNode

    def insertAtTail(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head=newNode
            self.tail=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode

    def printList(self):
        if self.isEmpty():
            print("List is empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data)
                temp=temp.next


ll1 = LinkedList()
ll1.insertAtHead(20)
ll1.insertAtHead(10)
ll1.insertAtTail(30)
ll1.printList()

