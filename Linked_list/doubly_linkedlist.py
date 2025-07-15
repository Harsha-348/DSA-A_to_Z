''' Doubly linked list --
Insert atbegin,
Insertatend,
specificposition, 
deleteatbegin,
deleteatend,
deleteatspecificposition
'''
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = DNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_at_position(self, position, data):
        if position == 0:
            self.insert_at_begin(data)
            return
        new_node = DNode(data)
        temp = self.head
        for _ in range(position - 1):
            if not temp:
                print("Position out of bounds")
                return
            temp = temp.next
        if not temp:
            print("Position out of bounds")
            return
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    def delete_at_begin(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    def delete_at_position(self, position):
        if not self.head:
            print("List is empty")
            return
        if position == 0:
            self.delete_at_begin()
            return
        temp = self.head
        for _ in range(position):
            if not temp:
                print("Position out of bounds")
                return
            temp = temp.next
        if not temp:
            print("Position out of bounds")
            return
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ⇄ ")
            temp = temp.next
        print("None")
