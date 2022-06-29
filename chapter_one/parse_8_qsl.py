from urllib.parse import parse_qsl
# 将参数转换为由元组组成的列表
query = 'name=germey&age=25'
print(parse_qsl(query),type(parse_qsl((query))))