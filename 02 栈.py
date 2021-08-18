# -*- coding: utf-8 -*-
"""
Time : 2021/2/15 21:48
Author : snail
Software ：PyCharm
E-mail : zh1289732630@gmail.com
CSDN bolg : https://blog.csdn.net/snail9610

Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
isEmpty() 判断栈是否为空
size() 返回栈的元素个数
"""


class MyStack:
    """使用列表创建栈，列表右端作为栈顶端"""
    def __init__(self):
        self.stack = []

    def push(self, item):
        """在顶端添加元素"""
        self.stack.append(item)

    def pop(self):
        """移除顶端元素"""
        if not self.isEmpty():
            # 非空时移除
            return self.stack.pop()
        else:
            # 空时返回空列表
            return []

    def peek(self):
        """返回顶端元素"""
        if not self.isEmpty():
            # 非空时返回
            # value = self.stack[-1] 如果是空元素，则报错（超出索引）
            return self.stack[len(self.stack) - 1]
        else:
            # 空时返回空列表
            return []

    def size(self):
        """返回栈中元素的个数"""
        return len(self.stack)

    def isEmpty(self):
        """判度栈是否为空"""
        # if self.size() == 0:
        #     return True
        # else:
        #     return False

        return self.stack == []


if __name__ == "__main__":
    stack1 = MyStack()
    print(stack1.size())
    print(stack1.isEmpty())
    stack1.push(1)
    stack1.push(3)
    stack1.push(2)
    stack1.push(4)
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.peek())
