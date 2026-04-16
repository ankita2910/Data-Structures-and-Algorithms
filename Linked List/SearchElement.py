

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head= Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)

temp=head
key = 25
found = False
while temp is not None:
    if temp.data == key:
        print("Found")
        found = True
        break
    temp=temp.next

if not found:
    print("Not present")


