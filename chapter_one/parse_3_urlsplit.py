from urllib.parse import urlsplit
result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
print(result)

#和urlparse非常类似，只不过不再解析params这一部分，这个和路径path在一起了