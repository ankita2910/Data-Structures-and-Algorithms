
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def hasCycle(head) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
# Example usage:
# Creating a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next  # Creating a cycle
cycle_exists = ListNode.hasCycle(head)
print(cycle_exists)  # Output: True 
