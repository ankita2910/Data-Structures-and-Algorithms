class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class hashmapOfNodes:
    def findPairs(self, head, target):
        pairs = []
        # Store the data (numbers) in the set for O(1) lookup
        seen_data = set() 
        current = head

        if head is None:
            return pairs

        while current:
            rem = target - current.data
            
            # Check if the needed number has been seen already
            if rem in seen_data:
                # Use a tuple (current.data, rem) for the result
                pairs.append((current.data, rem))
            
            # Add current data to the set
            seen_data.add(current.data)
            current = current.next
            
        return pairs

if __name__=="__main__":
    head = Node(10)
    head.prev = None

    head.next = Node(20)
    head.next.prev = head

    head.next.next = Node(30)
    head.next.next.prev = head.next

    head.next.next.next = Node(40)
    head.next.next.next.prev = head.next.next

    head.next.next.next.next = Node(50)
    head.next.next.next.next.prev = head.next.next.next

    target = 50
    obj = hashmapOfNodes()
    List=obj.findPairs(head, target)
    print(List)