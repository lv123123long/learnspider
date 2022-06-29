from urllib.parse import quote
# 将内容转换成url编码的格式，解决url中带有中文导致乱码的问题
keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)

print(url)
