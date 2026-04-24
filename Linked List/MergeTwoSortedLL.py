class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class MergeSortedLL:
    def merge(self,head1,head2):
        ptr1=head1
        ptr2=head2
        org_dummy=Node(0)
        dummy=org_dummy
        while ptr1 != None and ptr2 != None:
            if ptr1.data < ptr2.data:
                dummy.next=ptr1
                ptr1=ptr1.next
            elif ptr1.data == ptr2.data:
                dummy.next=ptr1
                ptr1=ptr1.next
                ptr2=ptr2.next
            else:
                dummy.next=ptr2
                ptr2=ptr2.next
            dummy=dummy.next

        if ptr1:
            dummy.next=ptr1
        if ptr2 != None:
            dummy.next=ptr2
            
        return org_dummy.next

if __name__ == "__main__":


    head1=Node(10)
    head1.next=Node(100)
    head1.next.next=Node(100)
    head1.next.next.next=Node(30)
    head1.next.next.next.next=Node(40)
    head1.next.next.next.next.next=Node(50)
    head1.next.next.next.next.next.next=Node(50)
    head1.next.next.next.next.next.next.next=Node(50)
    head2=Node(10)
    head2.next=Node(100)
    head2.next.next=Node(100)
    head2.next.next.next=Node(30)
    head2.next.next.next.next=Node(40)
    head2.next.next.next.next.next=Node(50)
    head2.next.next.next.next.next.next=Node(50)
    head2.next.next.next.next.next.next.next=Node(50)
    obj = MergeSortedLL()
    merged_head = obj.merge(head1, head2)
    
    # Print logic to see result
    while merged_head:
        print(merged_head.data, end=" -> ")
        merged_head = merged_head.next