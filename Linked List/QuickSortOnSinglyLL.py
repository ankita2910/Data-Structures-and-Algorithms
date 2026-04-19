class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
     
class QuickSort:
    
    def Quick_Sort(self, head,tail):
        if head is None or head==tail or head == tail.next:
            return
        pre_pI = head
        pI= self.partition(head,tail)
        while pre_pI and pre_pI.next != pI:
            pre_pI = pre_pI.next

        self.Quick_Sort(head,pI)
        self.Quick_Sort(pI.next, tail)

    def partition(self, head,tail):
        pivot=head.data
        pre=head
        curr=head.next
        while curr!=tail.next:
            if curr.data < pivot:
                pre = pre.next
                pre.data, curr.data=curr.data,pre.data
            curr=curr.next

        head.data,pre.data = pre.data,head.data
        return pre

if __name__ == "__main__":
    head=Node(100)
    head.next=Node(20)
    head.next.next=Node(10)
    head.next.next.next=Node(30)
    head.next.next.next.next=Node(5)
    head.next.next.next.next.next=Node(50)
    head.next.next.next.next.next.next=Node(40)
    head.next.next.next.next.next.next.next=Node(20)
    low=head
    tail=head
    while tail.next is not None:
        tail=tail.next
    
    obj=QuickSort()
    obj.Quick_Sort(head, tail)

    temp=head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next