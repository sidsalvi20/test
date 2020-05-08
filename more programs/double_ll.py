class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList(Node):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def prepending(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            newnode.prev = None

    def deletenode(self,value):
        
        current = self.head
        if current.data == value:
            current.next = self.head
        elif current!=None:
            while current!=None and current.data!=value:
                prev = current
                current.next.prev = prev
                current = current.next
                
            prev.next = current.next
        else:
            print("Node Was Not Found")
            
            
    def display(self):
        current = self.head
        print("DATA:")
        if current == None:
            print("There is no data in the linked list")
        else:
            while(current!=None):
                
                print(current.data)
                current = current.next

l1 = LinkedList()
print("DOUBLE LINKED LIST")
print("Enter Your Choice:")
print("1)Enter The Node")
print("2)Delete The Node")
print("3)EXIT Process")
choice = int(input())
while choice!=3:
    if choice == 1:
        d = int(input("Enter The Data To Be Added"))
        l1.prepending(d)
        l1.display()
        print("Enter Your Choice:")
        print("1)Enter The Node")
        print("2)Delete The Node")
        print("3)EXIT Process")
        choice = int(input())

    elif choice == 2:
        v = int(input("Enter The Value To Be Deleted"))
        l1.deletenode(v)
        print("The Updated Linked List is:")
        l1.display()
        print("Enter Your Choice:")
        print("1)Enter The Node")
        print("2)Delete The Node")
        print("3)EXIT Process")
        choice = int(input())

