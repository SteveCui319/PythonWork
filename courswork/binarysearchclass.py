class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # getter and setter for data
    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    # getter and setter for left node
    def get_left(self):
        return self.left

    def set_left(self, node):
        self.left = node

    # getter and setter for right node
    def get_right(self):
        return self.right

    def set_right(self, node):
        self.right = node


class BinarySearchTree:
    def __init__(self, limit):
        self.root = None
        self.limit = limit
        self.size = 0

    def is_empty(self):
        """Check if the tree is empty."""
        return self.root is None

    def is_full(self):
        """Check if the tree is full based on limit."""
        return self.limit is not None and self.size >= self.limit

    def insert(self, data):
        """Insert data into the tree."""
        if self.is_full():
            print("The tree is full.")
            return

        if self.is_empty():
            # if the tree is empty, set the new node to the root
            self.root = TreeNode(data)
        else:
            self.insert_recursive(self.root, data)

        self.size += 1
        print(f"Inserted {data} into the tree.")

    def insert_recursive(self, node, data):
        # if the new node smaller than current node, insert to left subtree
        if data <= node.get_data():
            # if the left subtree got no nodes, set the new node
            if node.get_left() is None:
                node.set_left(TreeNode(data))
            else:
                self.insert_recursive(node.get_left(), data)

        # if the new node bigger than current node, insert to right subtree
        else:
            if node.get_right() is None:
                node.set_right(TreeNode(data))
            else:
                self.insert_recursive(node.get_right(), data)

    def traverse(self):
        """Traverse the tree in ascending order and return list of elements."""
        nodes_list = []
        self.in_order_traversal(self.root, nodes_list)
        return nodes_list

    # Left -> Root -> Right
    def in_order_traversal(self, node, elements):
        if node:
            self.in_order_traversal(node.get_left(), elements)
            elements.append(node.get_data())
            self.in_order_traversal(node.get_right(), elements)

    def print_tree(self):
        """Print a visual representation of the tree."""
        if self.is_empty():
            print("The tree is empty.")
        else:
            nodes = self.traverse()
            print(" -> ".join(map(str, nodes)))


obj_bst = BinarySearchTree(limit=5)

# insert the node
obj_bst.insert(10)
obj_bst.insert(20)
obj_bst.insert(5)
obj_bst.insert(42)
obj_bst.insert(1)
obj_bst.insert(23)

print("information of tree:")
obj_bst.print_tree()

