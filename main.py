#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 下午4:56
# @Author  : Aries
# @Site    : 
# @File    : main.py
# @Software: PyCharm Community Edition
import logging
import time
import random
import json
import traceback
from retry import retry
from requests import request
from requests import HTTPError
from excel_helper import ExcelHelper
logger = logging.getLogger(__name__)


JSONCALLBACK = 'jsonpCallback9145'


class HTTPError(Exception):
    pass


@retry(HTTPError, tries=10, delay=3)
def request_http(url, headers, postdata=None, timeout=60):
    """
    http请求函数
    :param url: 
    :param headers: 
    :param postdata: 
    :param timeout: 
    :return: str, str
    """
    if postdata:
        method = 'POST'
    else:
        method = 'GET'
    if not url.startswith('http'):
        url = 'https://' + url
    result = request(
        method=method,
        url=url,
        headers=headers,
        data=postdata,
        timeout=timeout,
        verify=False
    )
    if not check_error(result):
        raise HTTPError()
    time.sleep(random.uniform(0, 2))
    return result.content, result.encoding, result.headers


def check_error(r):
    """
    :param r: response object
    :return: Bool
    """
    if r.status_code == 200 and r.content and r.encoding:
        return True
    else:
        return False


def start(max_page):
    url = 'http://query.sse.com.cn/commonQuery.do?&jsonCallBack=%s&isPagination=true' \
          '&sqlId=COMMON_SSE_GP_SJTJ_FHSG_AGFH_L_NEW&pageHelp.pageSize=25&pageHelp.pageNo=%d&pageHelp.beginPage=%d' \
          '&pageHelp.endPage=%d&pageHelp.cacheSize=1&record_date_a=2018&security_code_a=&_=1539851334638'

    result_filename = time.strftime('%Y%m%d%H%M%S', time.localtime()) + '.xlsx'
    referer_header = {'Referer': 'http://www.sse.com.cn/market/stockdata/dividends/dividend/'}
    final_result = [['股票代码', '股票简称', '公司名称', '税前每股红利', '税后每股红利', '股权登记日', '除息日']]
    for i in range(1, max_page + 1):
        print('i: %d' % i)
        content = ''
        request_url = url % (JSONCALLBACK, i, i, max_page)
        print(request_url)
        try:
            content, encoding, header = request_http(url=request_url, headers=referer_header)
            content = content.decode(encoding)
        except Exception:
            print('request_url error: %s' % request_url)
            traceback.print_exc()
        result = deal_content(content)
        if result:
            final_result = final_result + result
        time.sleep(random.uniform(1, 4))
    data_to_excel(result_filename, final_result)


def data_to_excel(result_filename, final_result):
    """
    :param result_filename: 结果文件名 
    :param final_result: 结果文件，list类型
    :return: None 
    """
    eh = ExcelHelper(result_filename)
    eh.insert_data(final_result)
    eh.save_excel()


def deal_content(content):
    """
    :param content: str类型 http返回数据
    :return:  list
    """
    result = []
    if not content:
        return result
    content = content[len(JSONCALLBACK)+1: -1]
    content_dic = json.loads(content)
    data = content_dic['pageHelp']['data']
    for value in data:
        result.append([value['COMPANY_CODE'], value['SECURITY_ABBR_A'], value['FULL_NAME'],
                      value['DIVIDEND_PER_SHARE2_A'], value['DIVIDEND_PER_SHARE1_A'],
                      value['RECORD_DATE_A'], value['EX_DIVIDEND_DATE_A']])
    return result


if __name__ == '__main__':
    max_page = 44  # 修改爬取页面长度，当前为44页
    start(44)
