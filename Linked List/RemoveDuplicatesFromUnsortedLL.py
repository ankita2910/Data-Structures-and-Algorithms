class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head=Node(12)
head.next=Node(11)
head.next.next=Node(12)
head.next.next.next=Node(21)
head.next.next.next.next=Node(41)
head.next.next.next.next.next=Node(43)
head.next.next.next.next.next.next=Node(21)

def RemoveDuplicates(head):
    st = set()
    temp=head
    prev = None

    while temp is not None:
        if temp.data in st:
            prev.next = temp.next
        else:
            st.add(temp.data)
            prev=temp
        temp=temp.next
    return head
RemoveDuplicates(head)

while head is not None:
    print(head.data)
    head=head.next

