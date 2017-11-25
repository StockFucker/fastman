#  -*- coding: utf-8 -*-

import urllib
import urllib2
import pandas as pd
import json

class Fastman(object):
    def __init__(self):
        self.url = 'http://183.57.48.75/stockapp/pstock/api/appstockshow.php?appn=3G&stktype=qq&grpid=0&format=json&r=1897&_deviceid=19df3d659336875789d4c03c790f7573c10c4190&_version=5.1.0_appver=5.1.0&_osystem=ios&isdelay=1&_rndtime=1511507734&_appName=ios&_dev=iPhone6,1&_devId=19df3d659336875789d4c03c790f7573c10c4190&_appver=5.1.0&_ifChId=&_isChId=1&_osVer=8.2&_uin=228588545&_wxuin=228588545'
        self.headers =  {"Host":"proxy.finance.qq.com","Accept":"*/*","Accept-Language":"zh-cn","Referer":"http://zixuanguapp.finance.qq.com","User-Agent":"QQStock/16081718 CFNetwork/711.2.23 Darwin/14.0.0"}

    def formate_stocks(self,stocks):
        form_stocks = []
        for stock in stocks:
            if stock[0] == "6":
                form_stocks.append("sh"+stock)
            elif stock[0] == "0" or stock[0] == "3":
                form_stocks.append("sz"+stock)
        return "|".join(form_stocks)

    #返回数据包和是否交易时间
    def get_quotes(self,stocks,dataFrame=True):
        stocks_str = self.formate_stocks(stocks)

        body = {'code':stocks_str}
        data_urlencode = urllib.urlencode(body)

        req = urllib2.Request(url = self.url,data =data_urlencode,headers = self.headers)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        data = json.loads(res)
        if data["code"] == 0:
            is_tradetime = data["data"]["market_stat"]["sh"] != "close"
            if dataFrame:
                df = pd.DataFrame(data["data"]["list"])
                columns = [u'amount', u'code', u'turnover_ratio', u'isdelay', u'name', u'sclx', u'state',u'symbol', u'cap', u'time', u'tips', u'type', u'volume', u'change', u'change_pct',u'pre_close', u'price']
                df.columns = columns
                return df,is_tradetime
            else:
                return data["data"]["list"],is_tradetime

if __name__ == "__main__":
    fastman = Fastman()
    print fastman.get_quotes(["000001","600001"])