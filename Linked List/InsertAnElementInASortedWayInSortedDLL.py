#If there are multiple keys to be inserted, then you do not have to change anything in the InsertSortedWay function
#Instead you save those keys in a list and call the function from main logic.

#Mistakes to avoid:
#The infinite loop is happening because of a logic error in your Middle Insertion block.
#Inside the if current.data <= key <= current.next.data: block, you insert the node, but you don't stop the loop. '
#'Because you've updated current.next to be your new dummy node, and dummy.next points to the old next_node, the loop keeps moving forward, eventually reaching the new node again or repeating the insertion logic indefinitely.
#Why it was looping:
# You found the spot between 30 and 50.
# You inserted 40.
# You didn't break, so the code executed current = current.next.
# Now current is the node you just inserted (40).
# On the next iteration, the condition current.data <= key <= current.next.data might trigger again (since 40 <= 40 <= 50), or the "End Insertion" logic might trigger once it hits the end, creating a messy or infinite chain of nodes.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class InsertDLL:
    def InsertSortedWay(self, head, key):
        
        dummy=Node(key)

        #Handle empty list
        if head is None:
            return dummy
        
        #handle new head
        if key < head.data:
            dummy.next=head
            head.prev = dummy
            return dummy

        current = head
        while current:

            # Handle End Insertion (Key is largest)
            if current.next is None:
                current.next= dummy
                dummy.prev=current
                break

            #Handle middle insertion
            if current.data <= key <= current.next.data:
                next_node = current.next

                current.next = dummy
                dummy.prev=current
                
                dummy.next= next_node
                next_node.prev=dummy
                break
            current = current.next
        return head

if __name__ == "__main__":
    head = Node(10)

    head.next = Node(20)
    head.next.prev = head

    head.next.next = Node(30)
    head.next.next.prev = head.next

    head.next.next.next=Node(50)
    head.next.next.next.prev = head.next.next

    key = 40
    obj = InsertDLL()
    obj.InsertSortedWay(head, key)

    while head is not None:
        print(head.data)
        head=head.next


