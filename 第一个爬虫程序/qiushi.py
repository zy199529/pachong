#!/usr/bin/env python
# coding: utf-8

# In[27]:


import requests
import re
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'}
info_lists = []
def judgment_sex(class_name):
    if class_name == 'womenIcon':
        return '女'
    else:
        return '男'
def get_info(url):
    res = requests.get(url)
    ids = re.findall('<h2>(.*?)</h2>',res.text,re.S)#用户名
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>',res.text,re.S)#等级
    sexs = re.findall('<div class="articleGender (.*?)">',res.text,re.S)#性别
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>',res.text,re.S)
    #内容，.*?匹配空行
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>',res.text,re.S)
    comments = re.findall('<i class="number">(\d+)</i> 评论',res.text,re.S)
    for id,level,sex,content,laugh,comment in zip(ids,levels,sexs,contents,laughs,comments):
        data = {
            'id':id.strip(),
            'level':level,
            'sex':judgment_sex(sex),
            'content':content.strip(),
            'laugh':laugh,
            'comment':comment
        }
        info_lists.append(data)
urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,36)]
for url in urls:
    get_info(url)
print(info_lists)
# 写入到txt文件

for info_list in info_lists:
    fw = open("./qiushi.txt",'a+')
    try:
        fw.write(info_list['id']+'\n')
        fw.write(info_list['level']+'\n')
        fw.write(info_list['sex']+'\n')
        fw.write(info_list['content']+'\n')
        fw.write(info_list['laugh']+'\n')
        fw.write(info_list['comment']+'\n\n')
    except UnicodeEncodeError:
        pass


# In[ ]:




