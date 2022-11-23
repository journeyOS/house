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


import optparse

from scrapy import cmdline


def parseargs():
    usage = "usage: %prog [options] arg1 arg2"
    parser = optparse.OptionParser(usage=usage)

    buildoptiongroup = optparse.OptionGroup(parser, "git push to gerrit options")

    buildoptiongroup.add_option("-c", "--city", dest="city",
                                help="city", default="sh")
    buildoptiongroup.add_option("-t", "--type", dest="type",
                                help="type", default="ershoufang")
    buildoptiongroup.add_option("-d", "--district", dest="district",
                                help="district", default="jiading")

    parser.add_option_group(buildoptiongroup)

    (options, args) = parser.parse_args()

    return (options, args)


def main():
    (options, args) = parseargs()
    city = options.city.strip()
    type = options.type.strip()
    district = options.district.strip()

    cmdline.execute(
        "scrapy crawl lianjia --nolog -a city={} -a type={} -a district={}".format(city, type, district).split())
    return 0


if __name__ == "__main__":
    main()
