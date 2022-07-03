import re
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())
print(result.group(1))  # 输出第一个被()包围起来的匹配结果

# 贪婪  .*
# 非贪婪  .*?  不可以用来配置字符串末尾