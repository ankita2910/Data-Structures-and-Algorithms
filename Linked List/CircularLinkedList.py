
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

temp = head
while True:
    print(temp.data)
    temp=temp.next
    if temp == head:
        break
