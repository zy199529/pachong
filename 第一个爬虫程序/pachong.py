#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
res = requests.get('http://bj.xiaozhu.com/')#网站为小猪短租网北京地区网址


# In[5]:


print(res)#print(res.text)


# In[8]:


import requests
headers ={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'}
res = requests.get('http://bj.xiaozhu.com/',headers=headers)#定义请求头的requests
print(res)


# In[ ]:




