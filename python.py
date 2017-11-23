# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 10:56:25 2017
源文件是在知乎看到的一个图片文件, 敲了下来.
若是侵权, 告删!
@author: Administrator
"""

import os

def main():
    print('Hello world!')
    
    print("This is Alice's greeting.")
    print('This is Bob\'s greeting.')
    
    foo(5, 10)
    
    print('=' * 10)
    print("Current working directory is " + os.getcwd())
    
    counter = 0
    counter += 1
    
    food = ['apple', 'orange', 'cats']
    
    for i in food:
        print('I like to eat ' + i)
        
    print('Count to ten: ')
    for i in range(10):
        print(i)
        
    
def foo(param1, secondParam):
    res = param1 + secondParam
    
    print('%s plus %s is equal to %s' % (param1, secondParam, res))
    
    if res < 50:
        print('foo')
        
    elif(res>= 50) and ((param1 == 42)) or (secondParam == 24):
        print('moo')
        
    return res  # This is one-line comment.
    ''' A multi-line string, but can also be a multi-line comment. '''
    

if __name__ == '__main__':
    main()
    
