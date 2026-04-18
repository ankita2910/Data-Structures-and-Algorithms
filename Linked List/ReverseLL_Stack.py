class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse(head):
    stack = []
    temp = head
    while temp.next is not None:
        stack.append(temp)
        temp=temp.next
    head=temp

    #pop all the nodes and append to the linked list
    while stack:
        temp.next=stack.pop()
        temp = temp.next
    temp.next=None
    return head

head = Node(10)
head.next=Node(20)
head.next.next = Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
num=reverse(head)
temp=num
while temp is not None:
    print(temp.data)
    temp=temp.next
