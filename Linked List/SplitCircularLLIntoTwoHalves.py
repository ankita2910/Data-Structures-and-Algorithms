class Node:
    def __init__(self, data):
        self.data = data
        self.next=None

class SplitLL:
    def TwoHalves(self, head):
        slow=head
        fast=head
        while fast.next != head and fast.next.next != head:
            slow=slow.next
            fast=fast.next.next
        
        if fast.next.next == head:
            fast=fast.next
        
        head2=slow.next
        
        fast.next = head2

        slow.next=head
        
        return head,head2

if __name__=="__main__":
    head=Node(100)
    head.next=Node(20)
    head.next.next=Node(10)
    head.next.next.next=Node(30)
    head.next.next.next.next=Node(5)
    head.next.next.next.next.next=Node(50)
    head.next.next.next.next.next.next=Node(40)
    head.next.next.next.next.next.next.next=Node(20)
    head.next.next.next.next.next.next.next.next=Node(1)
    head.next.next.next.next.next.next.next.next.next=head
    obj=SplitLL()
    (a,b)=obj.TwoHalves(head)
    
    print("First Half:")
    curr = a
    while True:
        print(curr.data)
        curr=curr.next
        if curr == a:
            break

    print("\nSecond Half:")
    curr = b
    while True:
        print(curr.data)
        curr=curr.next
        if curr == b:
            break
        