#!/usr/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        if self.head != None:
            new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return

        p = self.head
        while p.next != None:
            p = p.next
        p.next = new_node

    def reverse(self):
        p = self.head
        if p == None:
            return
        
        p = self.head.next
        self.head.next = None

        next_node = None
        while p != None:
            next_node = p.next
            p.next = self.head
            self.head = p
            p = next_node

    def reverse2(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next

            current.next = prev
            prev = current

            current = next_node

        self.head = prev
          

    def print_list(self):
        p = self.head
        while p != None:
            print(p.data, end=' ')
            p = p.next
        print()


l = LinkList()

for i in range(1, 11):
    l.insert_tail(i)

l.print_list()

l.reverse2()

l.print_list()

          
            
