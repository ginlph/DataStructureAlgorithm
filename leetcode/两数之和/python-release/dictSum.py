#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lph time:2020/9/11


def twoSum(nums: list, target: int):
    _dict = {}
    for k, v in enumerate(nums):
        if target - v in _dict:
            return [_dict[target - v], k]
        _dict[v] = k


if __name__ == '__main__':
    arrayList = [2, 7, 11, 15]
    target = 9
    twoSum(arrayList, target)