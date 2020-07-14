#!/usr/bin/env python
# coding=utf-8

a = 12
b = 3


if a > b :
    print(str(a) + " >" + str(b))
else :
    print(str(a) + " <" + str(b))

print(a if a > b else b)
