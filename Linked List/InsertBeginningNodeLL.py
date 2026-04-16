

class Node:
    def __init__(self, data):
        self.data=data
        self.next = None

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)

new_data=Node(100)
temp = head

head= new_data
head.next=temp

var = head
while var is not None:
    print(var.data)
    var=var.next
