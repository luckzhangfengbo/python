#!/usr/bin/env python
# coding=utf-8
# TempStr = input("输入带有符号的温度值: ")
# if TempStr[-1] in ['F', 'f']:
#     C = (eval(TempStr[0:-1]) - 32) / 1.8
#     print("转换后的温度是{:.2f}C".format(C))
# elif TempStr[-1] in ['C', 'c']:
#     F = 1.8 * eval(TempStr[0:-1]) + 32
#     print("转换后的温度是{:.2f}F".format(F))
# else:
#     print("输入格式错误")


def tempconvert(valuestr):
    if valuestr[-1] in ['F', 'f']:
        c = (eval(valuestr[0:-1]) - 32) / 1.8
        print("转换后的温度是：{:.2f}C".format(c))
    elif valuestr[-1] in ['C', 'c']:
        f = 1.8 * eval(valuestr[0: -1]) + 32
        print("转换后的温度是{:.2f}C".format(f))
    else:
        print("输入格式错误")

TempStr = input("请输入有符号的温度值：")
tempconvert(TempStr)
