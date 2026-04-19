class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head=Node(10)
head.next=Node(100)
head.next.next=Node(100)
head.next.next.next=Node(30)
head.next.next.next.next=Node(40)
head.next.next.next.next.next=Node(50)
head.next.next.next.next.next.next=Node(50)
head.next.next.next.next.next.next.next=Node(50)


def RemoveDuplicates(head):
    prev=head
    temp=head.next

    while temp is not None:
        if temp.data == prev.data:
            prev.next=temp.next
            temp = temp.next
        else:
            prev=temp
            temp=temp.next
    return head

RemoveDuplicates(head)

while head is not None:
    print(head.data)
    head=head.next