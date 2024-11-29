import pytest

class Node:
    def __init__(self, node_id, data):
        self.node_id = node_id
        self.data = data
        self.left = None
        self.right = None













def test_node_initialization():
    node = Node("root", 10)
    assert node.node_id == "root"
    assert node.data == 10
    assert node.left is None
    assert node.right is None
