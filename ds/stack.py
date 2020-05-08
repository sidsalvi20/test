class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
        
        
    def push(self,data):
        newnode = Node(data)
        if self.top == None:
            self.top = newnode
            
        else:
            newnode.next = self.top
            self.top = newnode
    def pop(self):
        if self.top == None:
            print("The Stack is Empty")
        else:
            current = self.top
            self.top = current.next
            print("Popped value ",current.data)
    def display(self):
        current = self.top
        if current == None:
            print("Stack Is Empty")
        else:
            print("DATA")
            while(current!=None):
               print(current.data)
               current = current.next
s = Stack()
print("Enter The Choice:")
print("1)Push A Value")
print("2)Pop A Value")
print("3)EXIT THE PROCESS")
choice = int(input())

while choice!=3:
    if choice == 1:
        d = int(input("Enter The Value To Be Pushed"))
        s.push(d)
        s.display()
        print("Enter The Choice:")
        print("1)Push A Value")
        print("2)Pop A Value")
        print("3)EXIT THE PROCESS")
        choice = int(input())

    elif choice == 2:
        s.pop()
        s.display()
        print("Enter The Choice:")
        print("1)Push A Value")
        print("2)Pop A Value")
        print("3)EXIT THE PROCESS")
        choice = int(input())

    
        
        
                
