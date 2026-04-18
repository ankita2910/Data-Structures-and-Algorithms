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

head.next.next.next.next.next.next.next.next = head


temp=head
while True:
    print(temp.data)
    
    if temp.next == head:
        break
    temp = temp.next
