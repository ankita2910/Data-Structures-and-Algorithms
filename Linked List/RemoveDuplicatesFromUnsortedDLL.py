class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class RemoveDuplicates:
    def duplicatesDLL(self, head):
        if head is None:
            return head

        current = head
        seen_data = set()
        while current is not None:
            if current.data in seen_data:
                #save nodes of current's prev and next as follows
                prev_node = current.prev
                next_node = current.next

                #connect prev to next
                if prev_node:
                    prev_node.next = next_node

                #Connect next back to prev
                if next_node:
                    next_node.prev = prev_node
                
                #Move to the next node to check
                current = next_node
            
            else:
                #first time seeing this data
                seen_data.add(current.data)
                current = current.next
        return head



if __name__ == "__main__":
    head = Node(20)

    head.next = Node(50)
    head.next.prev = head

    head.next.next = Node(20)
    head.next.next.prev = head.next

    head.next.next.next=Node(10)
    head.next.next.next.prev = head.next.next

    head.next.next.next.next=Node(50)
    head.next.next.next.next.prev = head.next.next.next

    obj = RemoveDuplicates()
    obj.duplicatesDLL(head)

    while head is not None:
        print(head.data)
        head=head.next