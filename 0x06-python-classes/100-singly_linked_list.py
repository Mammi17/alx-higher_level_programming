#!/usr/bin/python3

"""Define classes for a singly-linked list."""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) != Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        c = ""
        current = self.head
        while current:
            c += str(current.data) + "\n"
            current = current.next_node
        return c[:-1]

    def sorted_insert(self, value):
        nouveau = Node(value)
        if not self.head:
            self.head = nouveau
            return

        if value < self.head.data:
            nouveau.next_node = self.head
            self.head = nouveau
            return

        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        if current.next_node:
            nouveau.next_node = current.next_node
        current.next_node = nouveau
