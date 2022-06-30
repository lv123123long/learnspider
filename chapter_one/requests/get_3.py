import requests
r = requests.get('https://scrape.center/favicon.ico')
print(r.text)    # 图片转换成字符串，所以乱码
print(r.content) # 图片转变成bytes类型的数据，二进制数据

with open('favicon.ico', 'wb') as f:
    f.write(r.content)