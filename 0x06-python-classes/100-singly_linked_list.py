#!/usr/bin/python3

"""This module contains a Node class which defines a node of
a singly linked list and a SinglyLinkedList class which is
a linear collection of  nodes

"""


class Node:
    """The Node class defines a node of a singly linked list

    Attributes:
        value: is value given by the user to be saved as data
    """
    def __init__(self, data, next_node=None):
        """The init method is called each time an instance of the Node class
        is created

        Args:
            data (int): the value to store in the node

        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self) -> int:
        """data property can be used to access private instance attribute
        of an object

        The getter is used to get the actual data hold in the Node object
        Returns:
            data (int): an integer

        The setter is used to set/reset the data in the a Node object to
        the given value
        Args:
            value (int): is the value to be saved in the node
        Raises:
            TypeError: if the given value is not an integer

        """
        return self.__data

    @data.setter
    def data(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node is node coming after the current one. His value
        is a Node object or None for the last node

        the getter is used to get the node coming after the current
        one
        Returns:
            a Node object

        the setter is used to set/reset the next node in a linked list
        Args:
            value (Node obj): identifier of the coming node
        Raises:
            TypeError: if the given value is not a Node object or None

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """The SinglyLinkedList class defines a singly linked list
    containing multiple nodes pointing to one another with the
    data sorted in increasing order

    """
    def __init__(self):
        """The __init__ method is called each time a new instance of
        the SinglyLinkedList class is created, to set the head_node
        to None

        """
        self.__head = None

    def sorted_insert(self, value):
        """This method is used to insert a new_node into the correct
        sorted position in the list

        Args:
            value:
                the value of the new_node to create and add to the
                linked list

        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next_node and value > temp.next_node.data:
                temp = temp.next_node
            if temp.next_node is None:
                temp.next_node = new_node
            else:
                new_node.next_node = temp.next_node
                temp.next_node = new_node

    def __str__(self) -> str:
        """The magic method __str__ is redefined here to return
        a string containing new line characters

        Return:
            a formatted string containing data of a linked list nodes
            and new line characters

        """
        curr = self.__head
        nodes_data: str = ""
        while curr:
            nodes_data += str(curr.data) + ('\n' if curr.next_node else '')
            curr = curr.next_node
        return nodes_data
