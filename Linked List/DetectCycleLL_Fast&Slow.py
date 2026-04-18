
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def detectCycle(head):
    slow=head
    fast=head
    if head == None or head.next == None:
        print("False")
    while True:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            print("Cycle detected")
            break
        if fast.next == None:
            print("False")
            break


head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
head.next.next.next.next.next=head

detectCycle(head)


