import re
content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', content)    # 转义字符
print(result)

# match  从头开始匹配
# search  匹配第一个符合要求的字符串
# findall  匹配所有符合要求的字符串，生成列表返回