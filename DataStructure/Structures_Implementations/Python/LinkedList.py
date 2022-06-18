class Node():
    def __init__(self):
        self.data = 0
        self.next = None

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def show_elements(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
            
    def lenght(self):
        result = 0
        current_node = self.head
        while current_node is not None:
            result += 1
            current_node = current_node.next
        return result

    def indexOf(self,index):
        result = 0
        current_node = self.head
        while current_node is not None and result != index:
            result += 1
            current_node = current_node.next
        return current_node

    def reverse(self):
        if self.head is None:
            return
    
        current_node = self.head
        prev_node = None
        
        while current_node is not None:
            # Track the next node
            next_node = current_node.next
            
            # Modify the current node
            current_node.next = prev_node
            
            # Update prev and current
            prev_node = current_node
            current_node = next_node
            
        self.head = prev_node



lista = LinkedList()

lista.append(10)
lista.append(20)
lista.append(30)

lista.show_elements()

print(lista.lenght())

print(lista.indexOf(2).data)

lista.reverse()

lista.show_elements()