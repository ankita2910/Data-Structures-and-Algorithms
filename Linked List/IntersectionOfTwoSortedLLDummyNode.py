class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head1=Node(10)
head1.next=Node(40)
head1.next.next=Node(70)
head1.next.next.next=Node(90)

head2=Node(20)
head2.next=Node(30)
head2.next.next=Node(40)
head2.next.next.next=Node(50)

def Intersection(head1,head2):
    dummy = Node(0)
    tail = dummy

    while head1 and head2:
        if head1.data>head2.data:
            head2=head2.next
        elif head1.data==head2.data:
            tail.next = Node(head1.data)
            tail=tail.next
            head1=head1.next
            head2=head2.next
        else:
            head1=head1.next
    return dummy.next


def printList(head):
    while head:
        print(head.data)
        head = head.next

res = Intersection(head1,head2)
printList(res)
