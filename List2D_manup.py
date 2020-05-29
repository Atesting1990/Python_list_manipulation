# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:46:33 2020

@author: Somyajit
"""

lst=[[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21],[22,23,24,25,26,27,28],[29,30,31,32,33,34,35],[36,37,38,39,40,41,42],[43,44,45,46,47,48,49]]

x=len(lst)
z=x-1
y=x//2

print('')       
print('Display of Hollow Square elements from given Matrix')
print('')    
for idx in range(x):
   if idx==0 or idx==z:
      print(lst[idx][:])
   else:
      print(lst[idx][0],lst[idx][x-1])
      
print('')
print('Display of Diamond elements from given Matrix')
print('')
for idx in range(x):
    if idx==0 or idx==z:
        print(lst[idx][y])
    elif idx<=y:
        p=y-idx
        q=y+idx
        print(lst[idx][p],lst[idx][q])
    else:
        r=y-(z-idx)
        s=y+(z-idx)
        print(lst[idx][r],lst[idx][s])
    continue
            
print('')
print('Display of central column/row elements from given Matrix')
print('')
for idx in range(x):
    if idx==y:
        print(lst[idx][:])
    else: 
        print(lst[idx][y])
    continue

print('')
print('Display of forward diagonal elements from given Matrix')
print('')
for idx in range(x):
    print(lst[idx][idx])
    
print('')
print('Display of reverse diagonal elements from given Matrix')
print('')
for idx in range(x):
    print(lst[idx][z-idx])   
            
print('')
print('Display of forward ascending triangle elements from given Matrix')
print('')
for idx in range(x):
    print(lst[idx][0:idx+1])
    
print('')
print('Display of forward descending triangle elements from given Matrix')
print('')
for idx in range(x):
    print(lst[idx][0:x-idx])       
        
print('')
print('Display of reverse ascending triangle elements from given Matrix')
print('')
for idx in range(x):
    print(lst[idx][z-idx:])
        
print('')
print('Display of reverse descending triangle elements from given Matrix')
print('')
for idx in range(x):
    print(lst[idx][idx:])
    
