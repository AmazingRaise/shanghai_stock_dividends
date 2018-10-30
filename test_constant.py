#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 下午3:05
# @Author  : Aries
# @Site    : 
# @File    : test_constant.py
# @Software: PyCharm Community Edition

query_header = {'Host': 'www.cninfo.com.cn',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Origin': 'http://www.cninfo.com.cn',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': 'http://www.cninfo.com.cn/cninfo-new/index',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Accept-Language': 'zh-CN,zh;q=0.9'}

query_body = 'keyWord=%s&maxNum=10&hq_or_cw=2'

check_exits_body = 'code=%s&market=%s&orgid=%s&type=%s&minYear=%s&maxYear=%s'

check_exits_header = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'www.cninfo.com.cn',
    'Origin': 'http://www.cninfo.com.cn',
    'Referer': 'http://www.cninfo.com.cn/cninfo-new/index',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive'

}

get_flag = {
    'Host': 'www.cninfo.com.cn',
    'Origin': 'http://www.cninfo.com.cn',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': 'text/plain, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
    'Referer': 'http://www.cninfo.com.cn/cninfo-new/index',
    'Accept-Language': 'zh-cn',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest'
}


download_header = {
    'Host': 'www.cninfo.com.cn',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://www.cninfo.com.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryWVbNeaMgqj8D2hVW',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://www.cninfo.com.cn/new/index',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9'}

download_body = '''------WebKitFormBoundaryMhKA2lIPKoK7gyXa
Content-Disposition: form-data; name="K_code"


------WebKitFormBoundaryMhKA2lIPKoK7gyXa
Content-Disposition: form-data; name="market"

%s
------WebKitFormBoundaryMhKA2lIPKoK7gyXa
Content-Disposition: form-data; name="type"

%s
------WebKitFormBoundaryMhKA2lIPKoK7gyXa
Content-Disposition: form-data; name="code"

%s
------WebKitFormBoundaryMhKA2lIPKoK7gyXa
Content-Disposition: form-data; name="orgid"

%s
------WebKitFormBoundaryMhKA2lIPKoK7gyXa
Content-Disposition: form-data; name="minYear"

%s
------WebKitFormBoundaryMhKA2lIPKoK7gyXa
Content-Disposition: form-data; name="maxYear"

%s
------WebKitFormBoundaryMhKA2lIPKoK7gyXa
Content-Disposition: form-data; name="hq_code"

%s
------WebKitFormBoundaryMhKA2lIPKoK7gyXa
Content-Disposition: form-data; name="hq_k_code"


------WebKitFormBoundaryMhKA2lIPKoK7gyXa
Content-Disposition: form-data; name="cw_code"

%s
------WebKitFormBoundaryMhKA2lIPKoK7gyXa
Content-Disposition: form-data; name="cw_k_code"


------WebKitFormBoundaryMhKA2lIPKoK7gyXa
Content-Disposition: form-data; name="hq_code"


------WebKitFormBoundaryMhKA2lIPKoK7gyXa
Content-Disposition: form-data; name="hq_k_code"


------WebKitFormBoundaryMhKA2lIPKoK7gyXa
Content-Disposition: form-data; name="cw_code"


------WebKitFormBoundaryMhKA2lIPKoK7gyXa
Content-Disposition: form-data; name="cw_k_code"


------WebKitFormBoundaryMhKA2lIPKoK7gyXa--
'''


down = '''------WebKitFormBoundaryWVbNeaMgqj8D2hVW
Content-Disposition: form-data; name="K_code"


------WebKitFormBoundaryWVbNeaMgqj8D2hVW
Content-Disposition: form-data; name="secrethide"


------WebKitFormBoundaryWVbNeaMgqj8D2hVW
Content-Disposition: form-data; name="secrethideyz"


------WebKitFormBoundaryWVbNeaMgqj8D2hVW
Content-Disposition: form-data; name="market"

sz
------WebKitFormBoundaryWVbNeaMgqj8D2hVW
Content-Disposition: form-data; name="type"

llb
------WebKitFormBoundaryWVbNeaMgqj8D2hVW
Content-Disposition: form-data; name="code"

300008
------WebKitFormBoundaryWVbNeaMgqj8D2hVW
Content-Disposition: form-data; name="orgid"

9900008271
------WebKitFormBoundaryWVbNeaMgqj8D2hVW
Content-Disposition: form-data; name="minYear"

2016
------WebKitFormBoundaryWVbNeaMgqj8D2hVW
Content-Disposition: form-data; name="maxYear"

2018
------WebKitFormBoundaryWVbNeaMgqj8D2hVW
Content-Disposition: form-data; name="cw-code"

300008
------WebKitFormBoundaryWVbNeaMgqj8D2hVW
Content-Disposition: form-data; name="start"

llb
------WebKitFormBoundaryWVbNeaMgqj8D2hVW
Content-Disposition: form-data; name="start1"

2016
------WebKitFormBoundaryWVbNeaMgqj8D2hVW
Content-Disposition: form-data; name="end1"

2018
------WebKitFormBoundaryWVbNeaMgqj8D2hVW
Content-Disposition: form-data; name="cw_k_code"


------WebKitFormBoundaryWVbNeaMgqj8D2hVW--
'''