
class Node:
    def __init__(self, data):
        self.data = data
        self.next=None


head = Node(10)
head.next=Node(20)
head.next.next = Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)

temp = head
count =0
while True:
    count+=1
    if temp.next == None:
        break
    print(temp.data)
    temp=temp.next
    
    

print(count)