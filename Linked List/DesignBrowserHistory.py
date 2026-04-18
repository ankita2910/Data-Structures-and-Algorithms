class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage):
        self.curr = Node(homepage)
    
    def visit(self, page):
        new_node = Node(page)

        #attach new node after the current node
        new_node.prev=self.curr
        self.curr.next=new_node

        #update current pointer
        self.curr= new_node
        return self.curr.data
    
    def back(self, back):
        temp = self.curr
        while temp.prev is not None and back:
            temp=temp.prev
            back = back - 1

        #update curr pointer
        self.curr = temp
        return self.curr.data

    def forward(self,forward):
        temp = self.curr
        while temp.next is not None and forward:
            temp=temp.next
            forward = forward - 1
        
        #update curr pointer
        curr = temp
        return self.curr.data

if __name__ == "__main__":
# Initialize with the homepage
    homepage = "gfg.org"
    obj = BrowserHistory(homepage)

    url = "google.com"
    obj.visit(url)

    url = "facebook.com"
    obj.visit(url)

    url = "youtube.com"
    obj.visit(url)

    print(obj.back(1))

    print(obj.back(1))

    print(obj.forward(1))

    obj.visit("linkedin.com")

    print(obj.forward(2))

    print(obj.back(2))

    print(obj.back(7))