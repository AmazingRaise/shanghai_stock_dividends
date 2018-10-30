#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 下午3:12
# @Author  : Aries
# @Site    : 
# @File    : test.py
# @Software: PyCharm Community Edition
import traceback
from requests import post
from main import request_http
from test_constant import *
from requests_toolbelt import MultipartEncoder


class InputData(object):

    def __init__(self, market, data_type, code, orgid, minyear, maxyear, starttime):
        self._market = market
        self._data_type = data_type
        self._code = code
        self._orgid = orgid
        self._minyear = minyear
        self._maxyear = maxyear
        self._starttime = starttime

    @property
    def market(self):
        return self._market

    @property
    def data_type(self):
        type_data = {
            '现金表': 'llb',
            '资产表': 'fzb',
            '利润表': 'lrb'
        }
        return type_data[self._data_type]

    @property
    def code(self):
        return self._code

    @property
    def orgid(self):
        return self._orgid

    @property
    def minyear(self):
        if int(self._starttime) > int(self._minyear):
            self._minyear = self._starttime
        return self._minyear

    @property
    def maxyear(self):
        return self._maxyear


def download_data(input_data):
    url = 'http://www.cninfo.com.cn/new/data/download'

    m = MultipartEncoder(
        fields={'K_code': None, 'secrethide': None, 'secrethideyz': None,
                'market': input_data.market, 'type': input_data.data_type, 'code': input_data.code,
                'orgid': input_data.orgid,
                'minYear': input_data.minyear,
                'maxYear': input_data.maxyear,
                'cw-code': input_data.code,
                'start': input_data.data_type,
                'start1': input_data.minyear,
                'end1': input_data.maxyear,
                'cw_k_code': None}
        )
    header = {
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Content-Type': m.content_type,
        'Referer': 'http://www.cninfo.com.cn/new/index',
    }

    res = post(url, headers=header, data=m)
    if res.status_code == 200:
        filename = res.headers['Content-Disposition']
        s = filename.find('filename=')
        filename = filename[s+len('filename='): len(filename)]
        with open('./' + filename, 'wb') as fp:
            fp.write(res.content)


def _query_orgId(stock_number):
    url = 'http://www.cninfo.com.cn/cninfo-new/data/query'
    header = query_header
    request_body = query_body % stock_number
    try:
        content, encoding, response_header = request_http(url, headers=header, postdata=request_body)
        content = content.decode(encoding)
        content = eval(content)
        for val in content:
            if val['code'] == stock_number:
                return val['orgId'], val['market'], val['startTime']
    except Exception:
        print('request_url error: %s' % url)
        traceback.print_exc()

if __name__ == '__main__':
    stock_number = '600004'
    orgid, market, starttime = _query_orgId(stock_number)
    input_data = InputData(market,
                           '利润表',
                           stock_number,
                           orgid, '1988', '2018', starttime
                           )
    download_data(input_data)
