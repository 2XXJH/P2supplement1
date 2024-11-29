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













def test_should_return_node_initialization():
    node = Node("root", 10)
    assert node.node_id == "root"
    assert node.data == 10
    assert node.left is None
    assert node.right is None
