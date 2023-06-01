#!/usr/bin/python3
"""Singly Linked List Implementation"""


class Node:
    """Node defination for singly linked list

    Attributes:
        __data: node data
        __next_node: next node
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get node data"""
        return self.__data

    @data.setter
    def data(self, new_data):
        """set node data"""
        if type(new_data) is not int:
            raise TypeError("data must be an integer")
        self.__data = new_data

    @property
    def next_node(self):
        """get next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, new_node):
        if new_node is not None and type(new_node) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = new_node


class SinglyLinkedList:
    """Singly linked list Class

    Attributes:
        __head: points to the first node
    """

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node at the correct index for the list to be sorted

        Args:
            value: the data of the new node
        """
        node = Node(value)
        if self.__head is None:
            node.next_node = None
            self.__head = node
        elif self.__head.data > value:
            node.next_node = self.__head
            self.__head = node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            node.next_node = tmp.next_node
            tmp.next_node = node

    def __str__(self):
        """defines the string representation for the list"""
        list_data = []
        tmp = self.__head

        while tmp is not None:
            list_data.append(str(tmp.data))
            tmp = tmp.next_node

        return "\n".join(list_data)
