from datetime import date
from baidux.utils import test_cookies
from baidux import config
from baidux import BaiduIndex
import xlwt
book = xlwt.Workbook(encoding= 'utf-8')
cookies = 'input your own cookies'
print(test_cookies(cookies))
keywords = [['南开大学']]
print(config.PROVINCE_CODE)
print(config.CITY_CODE)
baidu_index = BaiduIndex(
keywords = keywords,
start_date='2021-06-29',
end_date = '2022-01-01',
cookies=cookies,
area=901)
sheet = book.add_sheet(keywords[0][0],cell_overwrite_ok=True)
dates=[]
indexs=[]
for index in baidu_index.get_index():
    print(index)
    dates.append(index['date'])
    indexs.append(index['index'])
for i in range(0,len(dates)):
    sheet.write(i,0,dates[i])
    sheet.write(i,1,index[i])
book.save('BAIDU.xls')