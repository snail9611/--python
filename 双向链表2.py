# -*- coding: utf-8 -*-
"""
Time : 2021/7/7 19:20
Author : snail
Software ： PyCharm 
E-mail : zh1289732630@gmail.com
CSDN bolg : https://blog.csdn.net/snail9610
"""


class Node:
    """双向链表节点"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doubly_linked_list:
    # Create the doubly linked list class
    def __init__(self):
        self.head = None

# Define the push method to add elements at the begining
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

# Define the append method to add elements at the end
    def append(self, NewVal):

        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return

# Define the method to print
    def listprint(self, node):
        while (node is not None):
            print(node.data),
            last = node
            node = node.next


dllist = doubly_linked_list()
dllist.push(12)
dllist.append(9)
dllist.push(8)
dllist.push(62)
dllist.append(45)
dllist.listprint(dllist.head)

