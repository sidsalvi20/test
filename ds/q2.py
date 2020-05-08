class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,data):
        newnode = Node(data)
        if self.front == None:
            self.front = newnode
            self.rear = newnode
        else:
            newnode.next = self.front
            self.front = newnode
    def dequeue(self):
        if self.rear == None:
            print("The queue is emppty")
        else:
            current = self.front
            while current.next!=None:
                prev = current
                current = current.next
            print("The deleted value is ",current.data)
            prev.next = None
    def display(self):
        current = self.front
        print("DATA")
        while current!=None:
            print(current.data)
            current = current.next

s = Queue()

print("Enter The Choice:")
print("1)Enqueue operation")
print("2)Dequeue Operation")
print("3)EXIT PROCESS")
choice = int(input())
while choice!=3:
    if choice == 1:
        d = int(input("Enter The Value To Be Added"))
        s.enqueue(d)
        s.display()
        print("Enter The Choice:")
        print("1)Enqueue operation")
        print("2)Dequeue Operation")
        print("3)EXIT PROCESS")
        choice = int(input())

    elif choice == 2:
        s.dequeue()
        s.display()
        print("Enter The Choice:")
        print("1)Enqueue operation")
        print("2)Dequeue Operation")
        print("3)EXIT PROCESS")
        choice = int(input())
