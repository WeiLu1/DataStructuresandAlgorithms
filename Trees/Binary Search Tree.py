from Nodes import Node as node
from collections import deque


class Tree:
    def __init__(self):
        self.root_node = None

    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current

    def find_max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child
        return current

    def insert(self, data):
        n = node(data)
        if self.root_node is None:
            self.root_node = n
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if n.data < current.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = n
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = n
                        return

    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return parent, None
        while True:
            if current.data == data:
                return parent, current
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child

    def remove(self, data):
        parent, node = self.get_node_with_parent(data)

        if parent is None and node is None:
            return False

        children_count = 0
        if node.left_child and node.right_child:
            children_count = 2
        elif (node.left_child is None) and (node.right_child is None):
            children_count = 0
        else:
            children_count = 1

        if children_count == 0:
            if parent:      # removing leaf node
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:   # removing a single node BST
                self.root_node = None

        elif children_count == 1:   # removing node with 1 child node
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child

            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node   # parent left node is now the deleted node left child
                else:
                    parent.right_child = next_node
            else:
                self.root_node = next_node

        # need to find inorder successor
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
            node.data = leftmost_node.data
            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child

    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                return None
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child

    def inorder_traversal(self, root_node):
        current = root_node
        if current is None:
            return
        self.inorder_traversal(root_node.left_child)
        print(current.data)
        self.inorder_traversal(root_node.right_child)

    def preorder_traversal(self, root_node):
        current = root_node
        if current is None:
            return
        print(current.data)
        self.preorder_traversal(root_node.left_child)
        self.preorder_traversal(root_node.right_child)

    def postorder_traversal(self, root_node):
        current = root_node
        if current is None:
            return
        self.postorder_traversal(root_node.left_child)
        self.postorder_traversal(root_node.right_child)
        print(current.data)

    def breadth_first_traversal(self):
        list_of_nodes = []
        traversal_queue = deque([self.root_node])
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            list_of_nodes.append(node.data)

            if node.left_child:
                traversal_queue.append(node.left_child)
            if node.right_child:
                traversal_queue.append(node.right_child)

        return list_of_nodes


def setup_tree():
    tree = Tree()
    n1 = node(6)
    tree.root_node = n1

    n2 = node(3)
    n3 = node(1)
    n4 = node(5)
    n5 = node(8)
    n6 = node(7)
    n7 = node(10)

    n1.left_child = n2
    n1.right_child = n5

    n2.left_child = n3
    n2.right_child = n4

    n5.left_child = n6
    n5.right_child = n7

    return tree


if __name__ == "__main__":

    tree = setup_tree()

    min = tree.find_min()
    max = tree.find_max()
    print(min.data)
    print(max.data)
