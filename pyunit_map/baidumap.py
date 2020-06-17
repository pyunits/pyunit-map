#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/14 9:06
# @Author: Jtyoui@qq.com
from math import ceil

import randomak


class BaiDuMap:
    """获取百度API地图"""

    def __init__(self, title=None, scope=None, page_size=20, page_num=0):
        """初始化

        :param title: 实体主题
        :param scope: 地址范围:必须具体到市区
        :param page_size: 返回一条是数据,默认是20,最大是20
        :param page_num: 页数
        """
        self.title = title
        self.scope = scope
        self.total_data = []
        self.json = []
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
        json = randomak.get_json(self.title, self.scope, page_size, page_num)
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
            if (self.scope not in address) and self.json == []:  # 获取地址不属于自己设置的地址
                if self.scope and (self.scope not in self.title):
                    self.title = self.scope + self.title
                else:
                    self.title = self.title
                self._get_data(page_size, page_num)
            else:
                self.total_data.append((name, location, address))
                self.json.append(json)

        if current_page < page:
            self._get_data(page_num=current_page)

    def save_txt(self, file_name):
        """保存到纯文本

        :param file_name: txt文件地址
        """
        with open(file_name, encoding='utf-8', mode='a') as f:
            for name, location, address in self.total_data:
                longitude = location.split('|')
                f.write(f'名字:{name}\t经度:{longitude[0]}\t纬度:{longitude[1]}\t地址:{address}\n')

    def get_pandas(self):
        """获得DataFrame类型"""
        names, longitude, latitude, addr = [], [], [], []
        for name, location, address in self.total_data:
            names.append(name)
            lg = location.split('|')
            longitude.append(lg[0])
            latitude.append(lg[1])
            addr.append(address)
        writer = {'名字': names, '经度': longitude, '纬度': latitude, '地址': addr}
        return writer

    def get_name(self):
        """获取实体名字"""
        return [name[0] for name in self.total_data]
