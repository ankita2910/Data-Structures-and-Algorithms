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

new_data = Node(1000)
key = 30
temp=head
given=head
while temp.data is not key:
    print("inside while")
    if temp.data == key:
        print("inside if")
        given=temp
        print(given.data,"given")
        break

    temp=temp.next


new_data.next =  given.next
given.next=new_data 


while head is not None:
    print(head.data)
    head=head.next
