# -*- coding: utf-8 -*-
"""
Time : 2021/7/7 10:29
Author : snail
Software ： PyCharm 
E-mail : zh1289732630@gmail.com
CSDN bolg : https://blog.csdn.net/snail9610
"""


class Node:
    """双向链表节点"""
    def __init__(self, item):
        self.item = item
        self.pre = None
        self.next = None


class DLinkList:
    """双向链表"""
    def __init__(self):
        self.head = None

    def isEmpty(self):
        """判断是否为空"""
        return self.head is None

    def length(self):
        """链表的长度"""
        cur = self.head
        l = 0
        while cur is not None:
            cur = cur.next
            l = l + 1

        return l

    def travel(self):
        """遍历链表，并打印数据"""
        cur = self.head
        while cur is not None:
            print(cur.item),
            cur = cur.next
        print(" ")

    def add_front(self, item):
        """在头部插入元素"""
        node = Node(item)
        node.next = self.head
        if not self.isEmpty():
            self.head.pre = node
        self.head = node

    def add_rear(self, item):
        """在尾部添加元素"""
        node = Node(item)
        node.next = None  # 最后一个节点的next是None
        if self.isEmpty():
            node.pre = None
            self.head = node
            return
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.pre = cur
            return

    def search(self, item):
        """查找元素是否存在"""
        cur = self.head
        while cur is not None:
            if cur.item is item:
                return True
            cur = cur.next
        return False

    def insert(self, pos, item):
        """在指定位置插入元素"""
        if pos <= 0:
            self.add_front(item)
        elif pos >= (self.length()-1):
            self.add_rear(item)
        else:
            node = Node(item)
            cur = self.head
            count = 0
            while count < (pos-1):
                count = count + 1
                cur = cur.next

            cur.next.pre = node
            node.next = cur.next

            cur.next = node
            node.pre = cur

    def remove(self, item):
        """删除指定元素"""
        if self.isEmpty():
            return
        else:
            cur = self.head
            if cur.item is item:
                # 如果首节点的元素是要删除的元素
                if cur.next is None:
                    # 如果链表只有这一个节点
                    self.head = None
                else:
                    # 将第二个节点的pre设置为None
                    cur.next.pre = None
                    # head指向第二个节点
                    self.head = cur.next
                return

            while cur is not None:
                if cur.item is item:
                    # 将cur前一个节点的next指向cur的后一个节点
                    cur.pre.next = cur.next
                    # 将后一个节点的pre指向前一个节点
                    cur.next.pre = cur.pre
                    break
                cur = cur.next


ll = DLinkList()
ll.add_front(1)
ll.add_front(2)
ll.add_rear(3)
ll.insert(2, 4)
ll.insert(4, 5)
ll.insert(0, 6)
print("length:", ll.length())
ll.travel()
print(ll.search(3))
print(ll.search(4))
ll.remove(1)
print("length:", ll.length())
ll.travel()








