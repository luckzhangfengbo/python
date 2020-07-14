#!/usr/bin/env python
# coding=utf-8
max_n = 10
l = list(range(0, max_n + 1))
for i in range(2, max_n):
    if l[i] == 0 :
        l[l[0]] = i  
        l[0] += 1
    for j in range(1, l[0]):
        if l[j] * i > max_n:
            break
            l[l[j] * i] = 1
        if i % l[j] == 0:
            break
print(l[max_n])
