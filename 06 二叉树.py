# -*- coding: utf-8 -*-
"""
Time : 2021/2/18 11:40
Author : snail
Software ：PyCharm
E-mail : zh1289732630@gmail.com
CSDN bolg : https://blog.csdn.net/snail9610
"""


# class MyNode:
#     """创建树节点"""
#     def __init__(self, item=None, leftChild=None, rightChild=None):
#         self.item = item
#         self.leftChild = leftChild
#         self.rightChild = rightChild


class MyBinaryTree:
    """创建二叉树"""
    def __init__(self,root=None):
        self.root = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,node):
        newNode = MyBinaryTree(node)
        if self.leftChild is None:
            self.leftChild = newNode
        else:
            newNode.leftChild, self.leftChild = self.leftChild, newNode

    def insertRight(self,node):
        newNode = MyBinaryTree(node)
        if self.rightChild is None:
            self.rightChild = newNode
        else:
            newNode.rightChild, self.rightChild = self.rightChild, newNode

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getRootVal(self):
        return self.root

    def setRootVal(self, node):
        self.root = node

    def preorder(self):
        """前序遍历"""
        print(self.root)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()


if __name__ == '__main__':
    tree = MyBinaryTree(0)
    tree.insertLeft(1)
    tree.insertRight(2)
    tree.insertRight(3)

'''
        s = 0
        queue = [root]
        
        while queue:
            if queue[0].val >= low and queue[0].val <= high:
                s += queue[0].val
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            
            queue.pop(0)
            
        return s
'''

# 12345
# 45123
