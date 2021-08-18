# -*- coding: utf-8 -*-
"""
Time : 2021/2/18 11:39
Author : snail
Software ：PyCharm
E-mail : zh1289732630@gmail.com
CSDN bolg : https://blog.csdn.net/snail9610
"""


class SingleNode:
    """"单链表的结点"""

    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList:
    """单链表"""

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def length(self):
        """链表长度"""
        cur = self.head  # 指向当前节点
        l = 0  # 长度
        while cur is not None:
            """未达到链表尾部时遍历"""
            l = l + 1
            cur = cur.next

        return l

    def travel(self):
        """遍历链表"""
        cur = self.head
        while cur is not None:
            print(cur.item)
            cur = cur.next

        print(" ")

    def add_front(self, item):
        """在头部添加元素"""
        node = SingleNode(item)
        node.next = self.head
        self.head = node  # 链表的头指向新节点

    def add_rear(self, item):
        """在尾部添加元素"""
        node = SingleNode(item)
        # 先判断链表是否为空，若为空则将头节点指向新节点
        if self.isEmpty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """在任意位置添加元素"""
        if pos <= 0:
            # 在头部
            self.add_front(item)
        elif pos > (self.length() - 1):
            # 在尾部
            self.add_rear(item)
        else:
            # 在中间任意位置
            node = SingleNode(item)
            cur = self.head
            count = 1
            while count < pos:
                count = count + 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """"删除节点"""
        cur = self.head
        pre = None
        while cur != None:
            if cur.item is item:
                if not pre:
                    # 如果第一个节点就是删除的节点
                    self.head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.head
        while cur is not None:
            if cur.item is item:
                return True
            cur = cur.next

        return False


# if __name__ == "__main__":
ll = SingleLinkList()
ll.add_front(1)
ll.add_front(2)
ll.add_rear(3)
ll.insert(2, 4)
print("length:", ll.length())
ll.travel()
print(ll.search(3))
print(ll.search(5))
ll.remove(1)
print("length:", ll.length())
ll.travel()
