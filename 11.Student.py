#!/usr/bin/env python
# coding=utf-8


class Student(object) :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print("%s : %d" %(self.name, self.age))
Stu1 = Student('jack', 22)
Stu2 = Student('bob', 23)


Stu1.show()
Stu2.show()


'''x = type(Stu1)
print(x)'''
