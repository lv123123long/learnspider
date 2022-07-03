import requests
r = requests.get('https://www.baidu.com')
print(r.cookies)
for key, value in r.cookies.items():     # 调用items()方法，将cookies转换成由元组组成的列表，遍历出每个cookie条目的名称和值
    print(key + '=' + value)