import requests
r = requests.get('https://www.baidu.com/')
print(type(r))   # 响应的类型

print(r.status_code,type(r.status_code))   #响应的状态码
print(r.text, type(r.text))   # 响应的内容
print(r.text[:100])    #  字符串前面一百个字符
print(r.cookies)   #响应的cookie
#print(r.json(), type(r.json()))