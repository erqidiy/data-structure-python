#!/usr/bin/python3

class Node:
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

def pre_order(root):
    if root != None:
        print(root.data, end=' ')
        pre_order(root.lchild)
        pre_order(root.rchild)

def in_order(root):
    if root != None:
        in_order(root.lchild)
        print(root.data, end=' ')
        in_order(root.rchild)

def post_order(root):
    if root != None:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=' ')

def layor_order(root):
    if root == None:
        return

    q = []
    p = None
    q.append(root)
    while len(q) > 0:
        p = q.pop(0)
        print(p.data, end=' ')

        if p.lchild != None:
            q.append(p.lchild)
        if p.rchild != None:
            q.append(p.rchild)

    print()

def height(root):
    if root == None:
        return 0

    left_height = height(root.lchild)
    right_height = height(root.rchild)

    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1

if __name__ == "__main__":
    a = Node('A', Node('B', Node('D', None, Node('F')), None), Node('C', None, Node('E')))
    print("PreOrder:")
    pre_order(a)
    print()

    print("InOder:")
    in_order(a)
    print()

    print("PostOrder:")
    post_order(a)
    print()

    print('LayorOrder:')
    layor_order(a)

    print("Tree height:", height(a))
