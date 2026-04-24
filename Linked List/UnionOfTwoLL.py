class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Union:
    def unionOfLL(self, head1,head2):
        st = set()

        result = None
        tail = None

        while head1:
            if head1.data not in st:
                st.add(head1.data)
                newNode = Node(head1.data)
            if not result:
                result = tail = newNode
            else:
                tail.next = newNode
                tail = newNode
            head1=head1.next
        
        while head2:
            if head2.data not in st:
                st.add(head2.data)
                newNode = Node(head2.data)
                if not result:
                    result = tail = newNode
                else:
                    tail.next= newNode
                    tail = newNode
            head2=head2.next
        return result
        

if __name__=="__main__":

    head1=Node(10)
    head1.next=Node(100)
    head1.next.next=Node(100)
    head1.next.next.next=Node(30)
    head1.next.next.next.next=Node(40)
    head1.next.next.next.next.next=Node(50)
    head1.next.next.next.next.next.next=Node(50)
    head1.next.next.next.next.next.next.next=Node(50)
    head2=Node(1)
    head2.next=Node(5)
    head2.next.next=Node(2)
    head2.next.next.next=Node(9)
    head2.next.next.next.next=Node(5)
    head2.next.next.next.next.next=Node(3)
    head2.next.next.next.next.next.next=Node(7)
    head2.next.next.next.next.next.next.next=Node(6)

    obj = Union()
    unionList = obj.unionOfLL(head1,head2)

    print("Union")
    
    while unionList is not None:
        print(unionList.data)
        unionList=unionList.next
