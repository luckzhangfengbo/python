#!/usr/bin/env python
# coding=utf-8


import math

'''def circle(r):
    result =  math.pi * r * r
    return result

r = float(input("请输入圆的半径:"))
print("半径为:" + str(r) + "圆的面积为多少:"+ str(circle(r)))
'''
r = float(input("请输入圆的半径:"))
result = lambda r : math.pi * r * r

print("半径为:", r , "圆的面积为 :", result(r))
