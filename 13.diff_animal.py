#!/usr/bin/env python
# coding=utf-8

'''多态性'''

class Animal(object):
    def __init__(self, name):
        self.name = name

    def say(self):
        print("{} is an Animal, I can say!".format(self.name))

class Cat(Animal):
    def say(self):
        print("{} is a cat, say '喵喵'!".format(self.name))

class Dog(Animal):
    def say(self):
        print("{} is a dog, say 'wang wang wang'!".format(self.name))


def Animal_say(animal):
    animal.say()
#传入animal的实例
Animal_say(Animal('a'))

#传入dog的实例
Animal_say(Dog('b'))
#传入cat的实例
Animal_say(Cat('c'))

