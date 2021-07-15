import time

import pandas as pd
import requests
import re
import json
#获取网页源代码：还是js文件
url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1#tab1"
response = requests.get(url)
response.encoding = 'utf-8'
res = response.text
#print(type(res))

#筛选出需要截取的js
data_list1 = re.findall(r'<script type="application/json" id="captain-config">(.*?)</script>', res)
for data in data_list1:  #type(data)=str
    continue
data_d = json.loads(data)   #js字符串转字典
#print(data_d)

#for key in data_d['component'][0]['trend']['list']:  #获取key得到最后数据块的key
 #   print(key)
#print(data_d['component'][0]["mapLastUpdatedTime"])    #映射上次更新时间

history = {}    #历史数据
data1 = data_d['component'][0]["trend"]
for i in data1:
    if i == 'updateDate':
        for j in range(len(data1['updateDate'])):
            dt = "2020." + data1['updateDate'][j]
            tup = time.strptime(dt, '%Y.%m.%d')
            dt = time.strftime('%Y-%m-%d', tup)    #改变时间格式
            confirm = data1['list'][0]['data'][j]
            confirm_add = data1['list'][4]['data'][j]
            suspect = data1['list'][1]['data'][j]
            suspect_add = data1['list'][5]['data'][j]
            crued = data1['list'][2]['data'][j]
            crued_add = data1['list'][6]['data'][j]
            died = data1['list'][3]['data'][j]
            died_add = data1['list'][7]['data'][j]
            history[dt] = {'confirm': confirm,'comfirned_add': confirm_add, 'suspect': suspect, 'suspect_add': suspect_add, 'crued': crued, 'crued_add': crued_add, 'died': died, 'died_add': died_add}
            if dt == '2020-12-31':
                break
        for j in range(341,len(data1['updateDate'])):
            dt = "2021." + data1['updateDate'][j]
            tup = time.strptime(dt, '%Y.%m.%d')
            dt = time.strftime('%Y-%m-%d', tup)    #改变时间格式
            if dt == '2020-12-31': break
            confirm = data1['list'][0]['data'][j]
            confirm_add = data1['list'][4]['data'][j]
            suspect = data1['list'][1]['data'][j]
            suspect_add = data1['list'][5]['data'][j]
            crued = data1['list'][2]['data'][j]
            crued_add = data1['list'][6]['data'][j]
            died = data1['list'][3]['data'][j]
            died_add = data1['list'][7]['data'][j]
            history[dt] = {'confirm': confirm,'comfirned_add': confirm_add, 'suspect': suspect, 'suspect_add': suspect_add, 'crued': crued, 'crued_add': crued_add, 'died': died, 'died_add': died_add}
details = []
update_time = data_d['component'][0]["mapLastUpdatedTime"]
data2 = data_d['component'][0]['caseList']
j=0
for i in data2:
        province = data2[j]['area']
        for k in range(len(data2[j]['subList'])):
            city = data2[j]['subList'][k]['city']
            confirm = data2[j]['subList'][k]['confirmed']
            confirm_add = data2[j]['subList'][k]['confirmedRelative']
            crued = data2[j]['subList'][k]['crued']
            dead = data2[j]['subList'][k]['died']
            details.append([update_time,province,city,confirm,confirm_add,crued,dead])
        j = j+1

pd.DataFrame(history).to_csv('历史数据.csv', index=0)
pd.DataFrame(details).to_csv('当日详细数据.csv', index=0)
print()