class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def swap(head):
    if head is None or head.next is None:
        return head
    new_head=head.next  #Second node becomes new head
    prev = None
    curr = head

    while curr and curr.next:

        first = curr
        second= curr.next

        #swap
        first.next=second.next
        second.next=first

        #connect previous pair
        if prev:
            prev.next=second
        
        #move pointers
        prev=first
        curr=first.next
    return new_head

head = Node(10)
head.next=Node(20)
head.next.next = Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
num=swap(head)

while num is not None:
    print(num.data)
    num=num.next
