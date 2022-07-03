import re
content1 = '2019-12-15 12:00'
content2 = '2022-12-15 11:00'
content3 = '2013-10-15 12:00'
pattern = re.compile('\d{2}:\d{2}')   #将字符串编译成 正则表达式对象   方便重复使用
result = re.sub(pattern, '', content1)
print(result)
