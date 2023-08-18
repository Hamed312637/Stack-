# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 23:25:24 2023

@author: hamed
"""

#Stack Using Array

class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1
    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.size-1
    
    def push(self, data):
        if self.is_full():
            raise Exception("Stack is overflow")
        else:
            self.top +=1 
            self.stack.append(data)
            
    def pop(self):
        if self.is_empty() :       
            raise Exception("Stack is underflow")
        else:
            item = self.stack[self.top]
            self.top -=1
            self.stack.pop()
            return item
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]
    
    def length(self):
        return len(self._stack)
    
    def print_stack(self):
        if self.is_empty():
            print('Stack is empty')
            return
        else:
            top = self.top
            while top >=0:
                print(self.stack[top])
                top -=1
        
st = Stack(10)             
st.push(5)
st.push(65)
st.push(25)
st.push(52)
st.push(55)
st.push(35)
st.pop()
st.print_stack()
print(st.peek())


   