class Node: 
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

    
#Create Linked List
head = Node(10)
head.next=Node(20)
head.next.next=Node(30)

# Print LL
temp =head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next
     
