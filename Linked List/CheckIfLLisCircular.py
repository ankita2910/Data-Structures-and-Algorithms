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
head.next.next.next.next.next.next.next.next=head

slow = head
fast = head.next

while True:

    if slow==fast:
        print("True")
        break
    else:
        if fast.next == None or head == None:
            print("False")
            break

    slow=slow.next
    fast=fast.next.next