#!/usr/bin/evn python
# coding:utf-8
__author__ = "benny"

import functools


def sys_hello(name):
    print("hello %s" % name)


def map_leran():
    # filter 返回一个可迭代的map对象
    result = map(lambda x: x * x, (1, 2, 3))
    print(type(result))
    for r in result:
        print(r)


def reduce_learn():
    '''
    reduce 方法移动到functools中去了
    :return:
    '''
    reduce1 = functools.reduce(lambda x, y: x + y, (1, 2, 3))
    print(reduce1)


def filter_learn():
    # filter 返回一个可迭代的filter对象
    result = filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6])
    print(type(result))
    for r in result:
        print(r)
    # print(list(result))


def sorted_learn():
    student = [("bobo", 49), ("lily", 68), ("kendy", 36), ("cody", 83)]
    sorted1 = sorted(student, key=lambda x: x[1], reverse=True)   # reverse=True 表示降序排列
    print(type(sorted1))
    print(sorted1)


if __name__ == "__main__":
    map_leran()
    reduce_learn()
    filter_learn()
    sorted_learn()
