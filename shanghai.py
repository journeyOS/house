#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-

# Copyright (c) 2022 anqi.huang@outlook.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from scrapy import cmdline

from house.base.net_utils import get_data


def get_city_info(city_id):
    """获取城市信息"""
    url = 'http://app.api.lianjia.com/config/config/initData'

    payload = {
        'params': '{{"city_id": {}, "mobile_type": "android", "version": "8.0.1"}}'.format(city_id),
        'fields': '{"city_info": ""}'
    }

    data = get_data(url, payload, method='POST')

    city_info = None
    for a_city in data['city_info']['info']:
        print('{} = {}'.format(a_city['city_name'], a_city['city_id']))
        if str(a_city['city_id']) == city_id:
            city_info = a_city
            break

    city_district = []
    for district in city_info['district']:
        district_quanpin = str(district['district_quanpin'])
        if 'shanghaizhoubian' == district_quanpin:
            print("don't need shanghai zhou bian")
        else:
            city_district.append(district_quanpin)

    return city_district


if __name__ == '__main__':
    # city_id = "310000"
    # city_info = get_city_info(city_id)
    #
    # for district in city_info:
    #     print('district = {}'.format(district))

    # 浦东
    # district = 'pudong'
    # 闵行
    # district = 'minhang'
    # 宝山
    # district = 'baoshan'
    # 徐汇
    # district = 'xuhui'
    # 普陀
    # district = 'putuo'
    # 杨浦
    # district = 'yangpu'
    # 长宁
    # district = 'changning'
    # 松江
    # district = 'songjiang'
    # 嘉定
    # district = 'jiading'
    # 黄浦
    # district = 'huangpu'
    # 静安
    # district = 'jingan'
    # 虹口
    # district = 'hongkou'
    # 青浦
    district = 'qingpu'
    # 奉贤
    # district = 'fengxian'
    # 金山
    # district = 'jinshan'
    # 崇明
    # district = 'chongming'

    # sf1a3a4a5p3
    # 限制只看普通住宅、70-130㎡、300-400W
    cmdline.execute(
        "scrapy crawl lianjia --nolog -a city=sh -a type=ershoufang -a district={} -a restrict=sf1a3a4a5p3".format(
            district).split())