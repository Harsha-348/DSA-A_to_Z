'''singly linked list --
Insert atbegin,
Insertatend,
specificposition,
deleteatbegin,
deleteatend,
deleteatspecificposition'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, position, data):
        if position == 0:
            self.insert_at_begin(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(position - 1):
            if not temp:
                print("Position out of bounds")
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_begin(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_at_position(self, position):
        if not self.head:
            print("List is empty")
            return
        if position == 0:
            self.delete_at_begin()
            return
        temp = self.head
        for _ in range(position - 1):
            if not temp.next:
                print("Position out of bounds")
                return
            temp = temp.next
        if not temp.next:
            print("Position out of bounds")
            return
        temp.next = temp.next.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")
