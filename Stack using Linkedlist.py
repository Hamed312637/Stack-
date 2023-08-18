# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 01:05:45 2023

@author: hamed
"""

# stack using linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def pop(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            return data
        else:
            raise Exception('Stack underflow')
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.head.data
    def print_stack(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
     
    def length_stack(self):
        if self.is_empty():
            return 0
        else:
            count =0
            node = self.head
            while node is not None:
                count +=1
                node = node.next
            return count    
    
    
st = Stack()
st.push(5)
st.push(6)
st.push(7)
st.push(8)
st.push(9)
st.pop()  
print(st.peek())
st.print_stack()
print(st.length_stack())      