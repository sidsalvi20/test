'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

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
            self.head = newnode

    def deletenode(self,value):
        
        current = self.head
        if current.data == value:
            current.next = self.head
        elif current!=None:
            while current!=None and current.data!=value:
                prev = current
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

'''

class LinkedList:
    li=list()
    def insertFront(self,obj):
        self.li.insert(index=0,object=obj)
    def insert(self,obj):
        self.li.append(obj)
    def deleteFront(self):
        list.pop(self.li,0)
    def deleteEnd(self):
        self.li.pop()
    def __str__(self):
        return self.li.__str__()
print("Linkedlist using list")
print("Enter the number of elements:")
num=int(input())
llist = LinkedList()
for i in range(0,num):
     print("Enter Elements:", end='')
     elem = input()
     llist.insert(elem)
print('List:')
print(llist)
print("Deleting element from front, List is now:")
llist.deleteFront()
print(llist)
print("Deleting element from end, List is now:")
llist.deleteEnd()
print(llist)

    
        
        
    
    

    

