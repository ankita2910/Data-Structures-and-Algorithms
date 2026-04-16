

class Node:
    def __init__(self, data):
        self.data = data
        self.next=None

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)

given = head.next.next.next
new_data = Node(60)

temp = given
new_data.next=given.next
temp.next=new_data



var=head
while True:
    
    if var is None:
        break
    print(var.data)
    var=var.next

