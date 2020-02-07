#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/14 9:06
# @Author: Jtyoui@qq.com
from pyunit_map import BaiDuMap, province


def test_only():
    """测试单一"""
    bd = BaiDuMap('健身房', '贵阳市')
    bd.save_execl('健身房')


def test_multiple():
    """测试多一地址"""
    bd = BaiDuMap()
    for p in province.GuiZhou:
        bd.update_title('健身房', p)
    bd.save_execl('健身房')


if __name__ == '__main__':
    # test_only()
    test_multiple()
