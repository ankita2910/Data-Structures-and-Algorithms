
class Node:
    def __init__(self, data):
        self.data= data
        self.next = None


head=Node(10)
head.next=Node(100)
head.next.next=Node(20)
head.next.next.next=Node(30)
head.next.next.next.next=Node(40)
head.next.next.next.next.next=Node(50)
head.next.next.next.next.next.next=Node(60)
head.next.next.next.next.next.next.next=Node(70)

k = 2
prev = None
count = 0
current = head
while current is not None:
    count += 1
    if count % k == 0:
        if prev is not None:
            prev.next = current.next
        else:
            head = current.next
    
    else:
        prev = current
    current = current.next

temp = head
while temp is not None:
    print(temp.data)
    temp=temp.next

