
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def middleNode(self, head) -> int:
        slowPntr = head
        fastPntr = head
        while(fastPntr != None and fastPntr.next != None):
            slowPntr = slowPntr.next
            fastPntr = fastPntr.next.next
        return slowPntr  
# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
middle_node = head.middleNode(head)

print(middle_node.val)