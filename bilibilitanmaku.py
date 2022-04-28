import requests
import pandas as pd
import re
 
def data_resposen(url):
    headers = {
        "cookie": "input your own cookies",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
    }
    resposen = requests.get(url,headers=headers)
    return resposen
 
def main(oid,month):
    df = pd.DataFrame()
    url = f'https://api.bilibili.com/x/v2/dm/history/index?month={month}&type=1&oid={oid}'
    list_data = data_resposen(url).json()['data']
    print(list_data)
    for data in list_data:
        urls = f'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid={oid}&date={data}'
        text = re.findall(".*?([\u4E00-\u9FA5]+).*?", data_resposen(urls).text)
        for e in text:
            print(e)
            data = pd.DataFrame({'弹幕':[e]})
            df = pd.concat([df,data])
 #please baidu to find how to transform a bv number to a oid.
if __name__ == '__main__':
    oid = '561820581' #视频id
    month = '2022-03' #开始日期
    main(oid,month)