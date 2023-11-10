#!/usr/bin/python3
"""
class module
"""


class Node:
    """
    node class module that defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """
        instantation
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        return data stored in the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        set data of the node
        parameters:
        @value: new value for the data(int).
        Raises:
        TypeError: if value is not an int
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        get the nest node in the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        set the next node in the linked list
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        self.__next_node = value


class SinglyLinkedList:
    """
    data structure
    """
    def __init__(self):
        """
        initialize an empty singly linked list
        """
        self.head = None

    def sorted_insert(self, value):
        """
        insert a new node into the correct sorted position in the list
        in increasing order
        """
        new_node = Node(value)

        if self.head is None or self.head.data > value:
            # insert at beginning of the list
            new_node.next_node = self.head
            self.head = new_node
        else:
            # traverse the list to find the correct position
            current = self.head
            while current.next_node
            is not None and current.next_node.data < value:
                current = current.next_node

            # insert new node into the sorted position
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        convert the linked list to a string for printing
        return string representation of of the linked list
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
