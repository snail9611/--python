# -*- coding: utf-8 -*-
"""
Time : 2021/2/16 14:06
Author : snail
Software ：PyCharm
E-mail : zh1289732630@gmail.com
CSDN bolg : https://blog.csdn.net/snail9610
"""
from MyCodes import MyStack


def parCheck(s):
    stack = MyStack()
    # if stack.isEmpty():
    #     Empty = False
    # else:
    #     return None
    pos = 0
    # Empty = False
    while pos < len(s):
        if s[pos] is '(':
            stack.push(s[pos])
        else:
            if stack.isEmpty():
                return False
            else:
                stack.pop()
        pos += 1

        if pos == len(s) and not stack.isEmpty():
            return False
        if pos == len(s) and stack.isEmpty():
            return True


if __name__ == '__main__':
    s = '())'
    print(parCheck(s))