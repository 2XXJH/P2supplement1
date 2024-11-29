import pytest

def test_node_initialization():
    node = Node("root", 10)
    assert node.node_id == "root"
    assert node.data == 10
    assert node.left is None
    assert node.right is None
