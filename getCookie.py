#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

userAgent  = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36';

#某个股 N年内 每天价格集合
def getCookie(url):
    _headers = {
        "User-Agent":userAgent,
    }
    _params = "";
    res = requests.get(url=url,params=_params,headers=_headers)
    #res.headers可以获取response的请求头哦
    return res.headers.get('Set-Cookie');


# cookie = getCookie('https://xueqiu.com/');
# print(cookie);



