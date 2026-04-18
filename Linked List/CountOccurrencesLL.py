class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head=Node(10)
head.next=Node(100)
head.next.next=Node(20)
head.next.next.next=Node(100)
head.next.next.next.next=Node(40)
head.next.next.next.next.next=Node(50)
head.next.next.next.next.next.next=Node(100)
head.next.next.next.next.next.next.next=Node(70)

count = 0
key=100
temp = head
while temp is not None:
    if temp.data == 100:
        count +=1
    temp = temp.next

print(count)