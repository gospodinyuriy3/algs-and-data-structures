class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue():
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        s = ""
        
        current = self.head
        while current:
            s += str(current.data)
            s += " "
            current = current.next
        
        return s[:-1]

    def push(self, data):
        node = Node(
            data=data
        )

        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        self.tail.next = node
        self.tail = node
        


    def pop(self) -> any:
        if self.head is None:
            return None
        
        result = self.head.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:   
            self.head = self.head.next

        return result

