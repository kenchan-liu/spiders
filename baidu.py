from datetime import date
from baidux.utils import test_cookies
from baidux import config
from baidux import BaiduIndex
import xlwt
cookies = 'input your cookies'
#print(test_cookies(cookies))
keywords = [['南开大学']]
print(config.PROVINCE_CODE)
print(config.CITY_CODE)
baidu_index = BaiduIndex(
keywords = keywords,
start_date='2021-06-29',
end_date = '2022-01-01',
cookies=cookies,
area=901)
dates=[]
indexs=[]
for index in baidu_index.get_index():
    print(index)
    dates.append(index['date'])
    indexs.append(index['index'])
import pandas as pd

c={"date": dates,"index": indexs}
df = pd.DataFrame(c)  #指定列名为name和id，顺序name先，id后

df.to_csv("baidu.csv")