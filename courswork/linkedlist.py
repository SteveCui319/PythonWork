class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, limit):
        self.head = None
        self.limit = limit
        self.size = 0

    def is_empty(self):
        return self.head is None

    def is_full(self):
        if self.limit is None:
            return False
        return self.size >= self.limit

    def __str__(self):
        if self.is_empty():
            return "The list is empty."
        data_list = []
        current_node = self.head
        while current_node is not None:
            data_list.append(str(current_node.get_data()))
            current_node = current_node.get_next()
        return " -> ".join(data_list)

    # receives a data value as a parameter and inserts it as a new node in the list
    def insert(self, data):
        if self.is_full():
            print("The list is full.")
            return False

        new_node = ListNode(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.size += 1
        return True






