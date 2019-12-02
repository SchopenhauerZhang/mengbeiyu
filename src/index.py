#!/usr/bin/env python3
import requests
url='https://movie.douban.com/' 
res=requests.get(url,timeout = (10,10)) 
print(res.status_code)