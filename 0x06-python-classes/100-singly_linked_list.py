#!/usr/bin/python3
""" a class to define a node of a singly linked list"""

class Node:
    """ a linked list node class"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = None

    @property
    def data(self):
        """propetry getter"""
        return self.__data
    @data.setter
    def data(self, value):
        if not isinstance (data, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next node getter"""
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        """next node setter"""
        if not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """singly linked list implementation"""
    def __init__(self):
        "instatiation"""
        self.__head = head
    if self.__head is None:
        print("list is empty")
    else:
        temp = self.__head
        while temp:
            print(temp.data)
            temp = temp.__next_node

    def def sorted_insert(self, value):
        """ inserts a new Node into the correct sorted position in the list (increasing order)"""
