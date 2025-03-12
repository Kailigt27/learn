# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 16:12:24 2025

@author: Asane
"""

'''
一个针对直接插入排序的练习
'''
def fastlist(list1):
    for i in range(1,len(list1)):
        if list1[i]<list1[i-1]:
            temp=list1[i]
            j=i-1
            while j>0 and temp<list1[j]:
                list1[j+1]=list1[j]
                j-=1
                list1[j+1]=temp
            
test = [1, 8, 2, 7]
fastlist(test)
for i in test:
    print(str(i) + " ", end="")