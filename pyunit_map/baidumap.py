#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/14 9:06
# @Author: Jtyoui@qq.com
import requests
from random import choice
from math import ceil
import pandas as pd


class BaiDuMap:
    """获取百度API地图"""

    def __init__(self, title=None, scope=None, page_size=20, page_num=0):
        """初始化

        :param title: 实体主题
        :param scope: 地址范围
        :param page_size: 返回一条是数据,默认是20,最大是20
        :param page_num: 页数
        """
        self.AK = [
            '8R82NkA5j2YzCO1hG2grXUxdLQnnHdVA',
            'mSYhaXLLGXffSkkgkalK84RV0Aof22vA',
            'OpYA7uSs7czqHw68w07ZzE9t08RQWrfO',
            'Tffez86k4u6rwGmE3MPR2N3XtUUNbZ7H',
            'rINxBQe6h4OGbmrLiImffAj96ZlhxCY8',
            'V6QYkOxaGwvU3WDVZKBdNUVjVvLcwQpH',
            'PKxVRcebGuDL4QsTtzFNMlCZ2rpfN3TG'
        ]
        self.title = title
        self.scope = scope
        self._total_data = []
        if title and scope:
            self._get_data(page_size, page_num)

    def update_title(self, title, scope, page_size=20, page_num=0):
        """更新主题和范围

        :param title: 实体主题
        :param scope: 地址范围
        :param page_size: 返回一条是数据,默认是20,最大是20
        :param page_num: 页数
        """
        self.title = title
        self.scope = scope
        self._get_data(page_size, page_num)

    def _get_data(self, page_size=20, page_num=0):
        """获取数据

        :param page_size: 返回一条是数据,默认是20,最大是20
        :param page_num: 页数
        :return: 主题信息集合
        """
        ak = choice(self.AK)  # 随机选取一个Ak值.AK要在百度接口上获取
        url = f'http://api.map.baidu.com/place/v2/search?query={self.title}&region={self.scope}&output=json&ak={ak}&page_size={page_size}&page_num={page_num}'
        json = requests.get(url).json()
        status = json.get('status')
        if status == 401:
            self._get_data(page_num=page_num)
            return
        elif str(status).startswith('3'):
            raise TypeError('该模块已经废弃不可用')
        results = json['results']  # 获取主要信息
        total = json['total']  # 获取总条数
        page = ceil(total / page_size)  # 取上整,获取页数
        current_page = page_num + 1  # 当前页数,应该等于上一页加1
        for result in results:
            name = result['name']
            locations = result['location']
            location = str(locations['lng']) + '|' + str(locations['lat'])
            address = result.get('province') + result.get('city') + result.get('area') + result.get('address')
            self._total_data.append((name, location, address))
        if current_page < page:
            self._get_data(page_num=current_page)
        print(json)

    def save_txt(self, file_name):
        """保存到纯文本

        :param file_name: txt文件地址
        """
        with open(file_name, encoding='utf-8', mode='a') as f:
            for name, location, address in self._total_data:
                f.write(f'名字:{name}\t经纬度:{location}\t地址:{address}\n')

    def get_pandas(self):
        """获得DataFrame类型"""
        names, loc, addr = [], [], []
        for name, location, address in self._total_data:
            names.append(name)
            loc.append(location)
            addr.append(address)
        writer = pd.DataFrame({'名字': names, '经纬度': loc, '地址': addr})
        return writer

    def save_execl(self, file_name: str):
        """保存到execl文件

        :param file_name: execl文件地址
        """
        writer = self.get_pandas()
        file_name = file_name + '.xlsx' if file_name.find('.') == -1 else file_name
        writer.to_excel(file_name, index=False)

    def get_name(self):
        """获取实体名字"""
        names = []
        for name in self._total_data:
            names.append(name[0])
        return names
