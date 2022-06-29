from urllib.parse import urlencode
params = {
    'name': 'germy',
    'age': '25'
}
base_url = 'https://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
# 将字典转换为 url的参数