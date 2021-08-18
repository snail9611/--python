# -*- coding: utf-8 -*-
"""
Time : 2021/2/15 13:13
Author : snail
Software ：PyCharm
E-mail : zh1289732630@gmail.com
CSDN bolg : https://blog.csdn.net/snail9610
"""
"""
逐字法、排序法、蛮力法、计数法
"""


def anagramSepar(s1, s2):
    """使用逐字法检测异序词"""
    alist2 = list(s2)
    pos1 = 0
    stillOK = True
    while stillOK and pos1 < len(s1):
        found = False
        pos2 = 0  # 每次s2从头开始
        while pos2 < len(alist2) and not found:
            """寻找相同的字母"""
            if s1[pos1] == alist2[pos2]:
                found = True  # 发现相同的字母，则退出循环
            else:
                pos2 += 1  # 没有发现，则检测s2下一个字母

        # 发现后标记为None，循环继续；否则返回False，程序结束
        if found:
            alist2[pos2] = None
        else:
            stillOK = False

        pos1 += 1

    return stillOK


def anagramSort(s1, s2):
    """使用排序法检测异序词"""
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()
    pos = 0
    stillOK = True
    while pos < len(alist1) and stillOK:
        if alist1[pos] == alist2[pos]:
            stillOK = True
            pos += 1
        else:
            stillOK = False

    return stillOK


def anagramCount(s1, s2):
    """使用计数法"""
    count1 = [0]*26
    count2 = [0]*26

    for i in range(len(s1)):
        """统计s1的字母"""
        pos = ord(s1[i]) - ord('a')
        count1[pos] += 1

    for i in range(len(s2)):
        """统计s2的字母"""
        pos = ord(s2[i]) - ord('a')
        count2[pos] += 1

    pos = 0
    stillOK = True
    while pos < 26 and stillOK:
        """匹配"""
        if count1[pos] == count2[pos]:
            pos += 1
        else:
            stillOK = False

    return stillOK

if __name__ == '__main__':
    s1 = 'python'
    s2 = 'typhon'
    s3 = 'abc'
    s4 = 'def'

    print(anagramCount(s1, s2))
    print(anagramCount(s3, s4))