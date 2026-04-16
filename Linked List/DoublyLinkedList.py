

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.prev = None
        self.next = None



head = Node(10)

head.next = Node(20)
head.next.prev = head

head.next.next = Node(30)
head.next.next.prev = head.next

head.next.next.next=Node(40)
head.next.next.prev = head.next.next

temp = head
while temp is not None:
    print (temp.data, end ="")
    if temp.next is not None:
        print("<->", end=" ")
    temp=temp.next