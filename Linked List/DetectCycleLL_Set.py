
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def detectCycle(head):
    st = set()

    if head in st:
        return True
    st.add(head)
    head=head.next
    return False

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
head.next.next.next.next.next=head

print(detectCycle(head))


