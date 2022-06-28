from urllib.parse import urlparse
result = urlparse('https://www.baidu.com/index.html;user?id=5#comment') # 对url进行解析
print(type(result))
print(result)  # 协议scheme 域名netloc 路径path ;参数params  ？查询条件query  #锚点fragment
# 返回的result是一个tuple，可以用属性名来访问，也可以用索引下表来访问