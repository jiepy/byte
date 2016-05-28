#!/usr/bin/env python
# ---------------------------
# author : Geng Jie
# email  : gengjie@outlook.com
#
# Create Time: 2016/3/8
# ---------------------------
# partial 函数说明，提前赋值函数中的一个参数
# filter 过滤条件是真的结果
#

from functools import partial


def bigger(x, y):
	return x > y


# 打印10以内大于三的数字

bigger3 = partial(bigger, y = 3)
result = list(filter(bigger3,range(10)))
print(result)