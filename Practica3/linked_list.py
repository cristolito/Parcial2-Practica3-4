from node import Node
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, student):
        new_node = Node(student)
        new_node.next_node = self.head
        self.head = new_node

        return student

    def get_list(self):
        current = self.head
        list = []
        while current:
            student = current.data
            list.append(student)
            current = current.next_node
        return list