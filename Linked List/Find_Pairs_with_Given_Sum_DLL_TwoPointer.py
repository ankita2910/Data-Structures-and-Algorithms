class Node:
    def __init__(self, data):
        self.data = data
        self.next =  None
        self.prev = None

class FindPairsDLL:
    def findpairs(self, head, left, right, target):
        if head is None:
            return None

        while left is not None and right is not None and left != right and right.next != left:
            current_sum = left.data + right.data
            if current_sum == target:
                return (left.data, right.data)
            elif current_sum < target:
                left = left.next
            else:
                right = right.prev
        return None


if __name__=="__main__":
    head=Node(10)
    head.prev=None

    head.next=Node(20)
    head.next.prev=head
    
    head.next.next=Node(30)
    head.next.next.prev = head.next
    
    head.next.next.next=Node(40)
    head.next.next.next.prev = head.next.next

    head.next.next.next.next=Node(50)
    head.next.next.next.next.prev = head.next.next.next

    left = head
    right = head
    while right.next is not None:
        right = right.next
    
    target = 50
    obj = FindPairsDLL()
    result = obj.findpairs(head, left, right, target)
    if result:
        print(f"Pair found: {result[0]}, {result[1]}")
    else:
        print("No pair found.")