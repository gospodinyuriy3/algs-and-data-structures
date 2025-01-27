import ctypes

class DynamicArray(object):
    def __init__(self, type):
        self.size = 0
        self.capacity = 1
        self.type = type
        self.array = self.make_array(self.capacity)

    def __str__(self) -> str:
        s = ""
        for i in range(self.size):
            s += f"{self.array[i]} "
        return s + "..."

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()
    
    def append(self, elem):
        if type(elem) != self.type:
            return TypeError
        
        if self.size == self.capacity:
            self.resize()
        
        self.array[self.size] = elem
        self.size += 1

    def resize(self):
        new_capacity = self.capacity * 2
        new_array = self.make_array(capacity=new_capacity)

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity
        #а потом первый массив мы удаляем из памяти, но с этим питончик уже как-то сам разберется       

    def len(self) -> int:
        return self.size
    
    def insert(self, elem, index):
        if type(elem) != self.type:
            return TypeError
        
        if index < 0 or index > self.size:
            return IndexError
        
        if self.size == self.capacity:
            self.resize()

        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = elem
        self.size += 1

    def index(self, elem) -> int:
        for i in range(self.size):
            if self.array[i] == elem:
                return i
            
            return ValueError

    def remove(self, index):
        if index < 0 or index > self.size - 1:
            return IndexError

        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        
        self.array[self.size - 1] = 0
        self.size -= 1
        
        if self.size == self.capacity / 4:
            self.capacity /= 2

    def pop(self, index) -> any:
        if index < 0 or index > self.size - 1:
            return IndexError

        result = self.array[index]

        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        
        self.array[self.size - 1] = 0
        self.size -= 1

        if self.size == self.capacity / 4:
            self.capacity /= 2

        return result
