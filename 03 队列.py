# -*- coding: utf-8 -*-
"""
Time : 2021/2/16 15:20
Author : snail
Software ：PyCharm
E-mail : zh1289732630@gmail.com
CSDN bolg : https://blog.csdn.net/snail9610
"""


class Queue:
    """使用列表构建队列：列表右端作为队头，左端作为队尾"""

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        """从队尾插入元素"""
        self.queue.insert(0, value)

    def dequeue(self, getback=False):
        """从队头删除一个元素"""
        if not getback:
            self.queue.pop()
        else:
            return self.queue.pop()

    def isEmpty(self):
        """判断是否为空队列"""
        return self.queue == []

    def length(self):
        """判断队列长度"""
        return len(self.queue)


class Dqueue():
    """双端队列"""
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def add_front(self, value):
        """从队头添加元素"""
        self.queue.append(value)

    def add_rear(self, value):
        """从队尾添加元素"""
        self.queue.insert(0, value)

    def remove_front(self, getback=False):
        """从队头删除元素"""
        if not getback:
            self.queue.pop()
        else:
            return self.queue.pop()

    def remove_rear(self, getback=False):
        """从队尾删除一个元素"""
        if not getback:
            self.queue.pop(0)
        else:
            return self.queue.pop(0)

    def length(self):
        return len(self.queue)


# if __name__ == "_main_":
q = Queue()
q.enqueue('hello')
q.enqueue('world')
q.enqueue('itcast')
print(q.length())
print(q.dequeue(getback=True))
print(q.dequeue(getback=True))
print(q.dequeue(getback=True))

deque = Dqueue()
deque.add_front(1)
deque.add_front(2)
deque.add_rear(3)
deque.add_rear(4)
print(deque.length())
print(deque.remove_front(getback=True))
print(deque.remove_front(getback=True))
print(deque.remove_rear(getback=True))
print(deque.remove_rear(getback=True))

