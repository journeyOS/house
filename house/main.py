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


from house.base.net_utils import get_data


def get_city_info(city_id):
    """获取城市信息"""
    url = 'http://app.api.lianjia.com/config/config/initData'

    payload = {
        'params': '{{"city_id": {}, "mobile_type": "android", "version": "8.0.1"}}'.format(city_id),
        'fields': '{"city_info": "", "city_config_all": ""}'
    }

    data = get_data(url, payload, method='POST')
    city_info = None
    for a_city in data['city_info']['info']:
        if str(a_city['city_id']) == city_id:
            city_info = a_city
            break

    for a_city in data['city_config_all']['list']:
        if str(a_city['city_id']) == city_id:
            city_info['city_abbr'] = a_city['abbr']
            break

    print(city_info)
    return city_info


if __name__ == '__main__':
    city_id = "310000"
    get_city_info(city_id)
