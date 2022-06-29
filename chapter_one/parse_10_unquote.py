from urllib.parse import unquote
# 将url编码格式解析
url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))