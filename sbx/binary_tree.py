from __future__ import annotations

import json
from typing import *

import pytest
from dotenv import load_dotenv

load_dotenv('.env')


class Node:
    data: Any
    left: Node
    right: Node

    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def add_left(self, data):
        self.left = Node(data)

    def add_right(self, data):
        self.right = Node(data)

    def rotate_left(self):
        """https://en.wikipedia.org/wiki/Tree_rotation
        
        Returns:
            Node: root of rotated tree
        """
        new_root = self.right
        new_left = self
        new_left_right = self.right.left

        new_root.right.left = None
        new_root.left = new_left
        new_root.left.right = new_left_right
        return new_root

    def rotate_right(self):
        """https://en.wikipedia.org/wiki/Tree_rotation
        
        Returns:
            Node: root of rotated tree
        """
        new_root = self.left
        new_right = self
        new_right_left = self.left.right

        new_root.left.right = None
        new_root.right = new_right
        new_root.right.left = new_right_left
        return new_root

    def __str__(self):
        return self.data

    def in_order(self, callback):
        if self is None:
            return
        else:
            if self.left is not None:
                self.left.in_order(callback)
            callback(self)
            if self.right is not None:
                self.right.in_order(callback)


class BST:
    root: Node

    def __init__(self, root=None):
        if root is None:
            self.root = None
        else:
            self.root = Node(data=root)

    def insert(self, data):
        pass

    def get(self, data):
        pass


@pytest.fixture
def L():
    L = Node('Q')
    L.left = Node('P')
    L.right = Node('C')
    L.left.left = Node('A')
    L.left.right = Node('B')
    return L


@pytest.fixture
def R():
    R = Node('P')
    R.left = Node('A')
    R.right = Node('Q')
    R.right.left = Node('B')
    R.right.right = Node('C')
    return R


def test_rotate_right(L, R):
    new_R = L.rotate_right()
    assert new_R.data == R.data
    assert new_R.left.data == R.left.data
    assert new_R.right.data == R.right.data
    assert new_R.right.left.data == R.right.left.data
    assert new_R.right.right.data == R.right.right.data


def test_rotate_left(L, R):
    new_L = R.rotate_left()
    assert new_L.data == L.data
    assert new_L.right.data == L.right.data
    assert new_L.left.data == L.left.data
    assert new_L.left.right.data == L.left.right.data
    assert new_L.left.left.data == L.left.left.data


def test_inverse(L, R):
    back = L.rotate_right().rotate_left()
    assert back.data == L.data
    back = R.rotate_left().rotate_right()
    assert back.data == R.data


def test_(L, R):
    x = []
    L.in_order(x.append)
    print(x)
    assert False
