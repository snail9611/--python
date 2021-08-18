# -*- coding: utf-8 -*-
"""
Time : 2021/2/3 11:02
Author : snail
Software ：PyCharm
E-mail : zh1289732630@gmail.com
CSDN bolg : https://blog.csdn.net/snail9610
"""


class SingleNode(object):
    """单链表的结点"""

    def __init__(self, item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self._head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur is not None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur is not None:
            print(cur.item)
            cur = cur.next
        print("")
