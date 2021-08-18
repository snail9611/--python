# -*- coding: utf-8 -*-
"""
Time : 2021/7/7 20:01
Author : snail
Software ： PyCharm 
E-mail : zh1289732630@gmail.com
CSDN bolg : https://blog.csdn.net/snail9610
"""


def quick_sort(alist):
    qsort(alist, 0, len(alist) - 1)
    return alist


def qsort(alist, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = alist[low]
    while left < right:
        while left < right and alist[right] > key:
            right -= 1
        alist[left] = alist[right]
        while left < right and alist[left] < key:
            left += 1
        alist[right] = alist[left]
    alist[right] = key

    qsort(alist, low, left-1)
    qsort(alist, left+1, high)


"""def partion(alist, low, high):
    pivot = alist[low]

    while low < high:

        while low < high and alist[high] >= pivot:
            high = high - 1
        alist[low] = alist[high]
        while low < high and alist[low] <= pivot:
            low = low + 1
        alist[low] = alist[high]

    return low"""


alist = [30,24,5,58,18,36,12,42,39]
print(alist)
print(quick_sort(alist))


