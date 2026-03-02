class ReverseLL:
    def __init__(self, value):
        self.value = value
        self.next = None

    def reverse_linked_list(self, head):
        if head.next is None or head is None:
            return head
        res = self.reverse_linked_list(head.next)
        head.next.next = head
        head.next = None
        return res
# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> None
head = ReverseLL(1)
head.next = ReverseLL(2)
head.next.next = ReverseLL(3)
# Reversing the linked list
reversed_head = head.reverse_linked_list(head)
# Printing the reversed linked list: 3 -> 2 -> 1 -> None
current = reversed_head
while current is not None:
    print(current.value)
    current = current.next


            


