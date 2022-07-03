import re
content = 'Hello 1234567 World_This \n is a Regex Demo'
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)   # re.S 将可以匹配换行符，这个叫修饰符
print(result.group(1))