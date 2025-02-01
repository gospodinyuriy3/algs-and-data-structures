class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(
            data=data
        )

        if self.top is None:
            self.top = node
            return

        node.next = self.top
        self.top = node

    def pop(self) -> any:
        if self.top is None:
            return None
        
        res = self.top

        if self.top.next is None:
            self.top = None
        else:
            self.top = self.top.next

        return res.data