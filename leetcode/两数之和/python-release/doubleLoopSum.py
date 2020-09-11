#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lph time:2020/9/11


def twoSum(nums: list, target: int) -> list:
    length = len(nums)
    # res = []
    for i in range(length):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                # res.append([i, j])
                return [i, j]
    # return res


if __name__ == '__main__':
    arrayList = [2, 7, 11, 15]
    target = 9
    print(twoSum(arrayList, target))