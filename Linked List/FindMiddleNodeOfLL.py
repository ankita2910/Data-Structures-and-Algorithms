

#Implemented Hare and Tortoise algorithm
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head=Node(10)
head.next=Node(100)
head.next.next=Node(20)
head.next.next.next=Node(30)
head.next.next.next.next=Node(40)
head.next.next.next.next.next=Node(50)
head.next.next.next.next.next.next=Node(60)
head.next.next.next.next.next.next.next=Node(70)

fast=head
slow=head
while fast is not None:
    fast=fast.next.next
    slow = slow.next

print(slow.data)