class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def reverse(self, head):
        curr = head
        prev = None
        while curr is not None:
            

            #reverse current node's next pointer
            new_node= curr.next
            curr.next=prev

            #move pointers one position ahead
            prev = curr
            curr = new_node
        return  prev



head = Node(10)
head.next=Node(20)
head.next.next = Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
num=head.reverse(head)
temp=num
while temp is not None:
    print(temp.data)
    temp=temp.next
