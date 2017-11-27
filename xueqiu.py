#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#上面的注释是用来支持中文，没有就会出错

import requests
import json
import sys 
import getCookie
import pandas as pd

class FastmanXQ(object):
    def __init__(self):
        self.stockInfoAPI = 'https://xueqiu.com/v4/stock/quote.json';
        cookieByJS = 'xq_a_token.sig=n7YA6AWL9rwg_LFe4waHpSmHqfM; xq_r_token.sig=S4AF23NdB-z6cYxfys3UTyBV6wk; device_id=2fea69b3e7f4d09a824841bb0edde4e1; s=fi18e4pdwv; xq_a_token=c191e96dce8a487e50e44332e2a7f1e3b103a959; xqat=c191e96dce8a487e50e44332e2a7f1e3b103a959; xq_r_token=d09b25c5ab1ba661d87789d873bede651505f3d9; xq_token_expire=Tue%20Dec%2012%202017%2023%3A02%3A36%20GMT%2B0800%20(CST); xq_is_login=1; u=1955492483; bid=14761af1b15c70d493f9806c0cb1e0d8_ja41a3fx; snbim_minify=true; __utma=1.1229010364.1510895903.1510931132.1510937343.5; __utmc=1; __utmz=1.1510937343.5.4.utmcsr=192.168.1.78:5000|utmccn=(referral)|utmcmd=referral|utmcct=/; isPast=true; isPast.sig=Q1zWad3glPfOy3Ye-506BMax-a0; Hm_lvt_1db88642e346389874251b5a1eded6e3=1510931241,1510937342,1510937776,1510938080; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1511160967'
        cookie = cookieByJS+getCookie.getCookie('https://xueqiu.com/');
        userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36';
        self.headers = {
            "User-Agent":userAgent,
            "Cookie":cookie
        }

    def formate_stocks(self,stocks):
        form_stocks = []
        for stock in stocks:
            if stock[0] == "6":
                form_stocks.append("SH"+stock)
            elif stock[0] == "0" or stock[0] == "3":
                form_stocks.append("SZ"+stock)
        return "%2C".join(form_stocks)

    #返回数据包
    def get_quotes(self,stocks,dataFrame=True):
        stocks_str = self.formate_stocks(stocks)
        _params = '&code=' + stocks_str;
        res = requests.get(url=self.stockInfoAPI,params=_params,headers=self.headers)
        data = json.loads(res.text)
        if dataFrame:
            df = pd.DataFrame(data)
            return df
        else:
            return data
        

if __name__ == "__main__":
    fastman = FastmanXQ()
    print fastman.get_quotes(["000001","600001"])