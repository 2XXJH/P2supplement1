import pytest

class Node:
    """
    A class representing a node in a binary tree.

    Attributes:
        node_id (str): Unique identifier for the node.
        data (int): Integer data stored in the node.
        left (Node): The left child of the node.
        right (Node): The right child of the node.
    """
    def __init__(self, node_id, data):
        """
        Initializes a Node with a unique ID and data.

        Args:
            node_id (str): Unique identifier for the node.
            data (int): Integer data to be stored in the node.
        """
        self.node_id = node_id
        self.data = data
        self.left = None
        self.right = None

    def insert(self, new_data):
        """
        Inserts new data into the binary tree following binary search tree rules.

        Args:
            new_data (int): The integer data to insert.
        
        Inserts:
            - If new_data is less than the current node's data, it goes to the left child.
            - If new_data is greater or equal, it goes to the right child.
            - Creates a new Node if the appropriate child does not already exist.
        """
        if new_data < self.data:
            if self.left is None:
                self.left = Node(f"{self.node_id}-L", new_data)
            else:
                self.left.insert(new_data)
        else:
            if self.right is None:
                self.right = Node(f"{self.node_id}-R", new_data)
            else:
                self.right.insert(new_data) 











def test_should_return_node_initialization():
    node = Node("root", 10)
    assert node.node_id == "root"
    assert node.data == 10
    assert node.left is None
    assert node.right is None

def test_insert_left():
    root = Node("root", 10)
    root.insert(5)
    assert root.left is not None
    assert root.left.data == 5
    assert root.left.node_id == "root-L"

def test_insert_right():
    root = Node("root", 10)
    root.insert(15)
    assert root.right is not None
    assert root.right.data == 15
    assert root.right.node_id == "root-R"

def test_insert_multiple_levels():
    root = Node("root", 10)
    root.insert(5)
    root.insert(15)
    root.insert(3)  # Goes to root.left.left
    assert root.left.left is not None
    assert root.left.left.data == 3
    assert root.left.left.node_id == "root-L-L"

def test_to_string():
    root = Node("root", 10)
    root.insert(5)
    root.insert(15)
    result = root.to_string()
    expected = (
        "ID: root, Data: 10\n"
        "\tID: root-L, Data: 5\n"
        "\tID: root-R, Data: 15\n"
    )
    assert result == expected


