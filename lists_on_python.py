class Node():
    def __init__(self, elem):
        self.data = elem
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self) -> str:
        s = ""
        current = self.head

        while current != None:
            s += str(current.data)
            s += ", "
            current = current.next

        return s[:-2]
    
    def len(self) -> int:
        return self.size
    
    def append(self, elem):
        node = Node(
            elem=elem
        )

        if self.head == None:
            self.head = node 
            self.size += 1
            return
            
        current = self.head
        while current.next != None:
            current = current.next

        current.next = node


        self.size += 1

    def insert(self, index: int, elem):
        if index < 0:
            return IndexError

        node = Node(
            elem=elem
        )

        if index >= self.size:
            self.append(elem=elem)
            return

        if index == 0:
            node.next = self.head
            self.head = node
            return
        
        current = self.head
        count = 0
        while current != None:
            if count == index:
                prev.next = node
                node.next = current
                break
            prev = current
            current = current.next
            count += 1
        
        self.size += 1

    def remove(self, elem):
        current = self.head
        prev = None

        while current != None:
            if current.data == elem:
                if prev == None:
                    self.head = current.next
                    self.size -= 1
                    return
                prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
        
    def reverse(self):
        curr = self.head
        prev = None

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def index(self, elem) -> int:
        current = self.head
        count = 0

        while current != None:
            if current.data == elem:
                return count
            current = current.next
            count += 1
        
        return ValueError


    def get(self, index) -> any:
        if index < 0 or index > self.size - 1:
            return IndexError
        
        count = 0
        current = self.head

        while current != None:
            if count == index:
                return current.data
            
            current = current.next
            count += 1
    
    def pop(self, index) -> any:
        if index < 0 or index > self.size - 1:
            return IndexError
        
        count = 0
        current = self.head
        prev = None

        while current != None:
            if count == index:
                if prev == None:
                    self.head = current.next
                    self.size -= 1
                    return current.data
                prev.next = current.next
                self.size -= 1
                return current.data
            
            prev = current
            current = current.next
            count += 1

class LinkedListWithTail:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def len(self) -> int:
        return self.size

    def append(self, elem):
        node = Node(
            elem=elem
        )

        if self.tail == None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        self.size += 1





class DoublyLinkedNode:
    def __init__(self, elem):
        self.data = elem
        self.next = None
        self.prev = None

    
class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self) -> str:
        s = ""
        current = self.head

        while current != None:
            s += str(current.data)
            s += ", "
            current = current.next

        return s[:-2]
    
    def len(self) -> int:
        return self.size
    
    def append(self, elem):
        node = DoublyLinkedNode(
            elem=elem
        )

        if self.head == None:
            self.head = node
            self.tail = node
            self.size += 1
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.size += 1
    
    def insert(self, index, elem):
        node = DoublyLinkedNode(
            elem=elem
        )

        if index >= self.size:
            self.append(elem=elem)
            return

        if index == 0 or index < -self.size:
            self.head.prev = node
            node.next = self.head
            self.head = node
            self.size += 1
            return
        
        if index < 0:
            index += self.size

        if index > self.size - index - 1:
            current = self.tail
            next = None
            count = self.size - 1
            while current != None:
                if count == index:
                    node.prev = current.prev
                    current.prev.next = node
                    current.prev = node
                    node.next = current
                    break
                next = current
                current = current.prev
                count -= 1
            
            self.size += 1
            return

        current = self.head
        prev = None
        count = 0
        while current != None:
            if count == index:
                prev.next = node
                node.prev = prev
                node.next = current
                current.prev = node
                break
            prev = current
            current = current.next
            count += 1
        
        self.size += 1

    def remove(self, elem):
        current = self.head
        prev = None

        while current != None:
            if current.data == elem:
                if prev == None:
                    self.head = current.next
                    self.size -= 1
                    return
                if next == None:
                    self.tail = prev
                    self.size -= 1
                    return
                prev.next = current.next
                current.next.prev = prev
                self.size -= 1
                return
            prev = current
            current = current.next

