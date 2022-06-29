from urllib.parse import parse_qs
query = 'name=germey&age=25'
print(parse_qs(query))

# 反序列化，将参数转换成字典