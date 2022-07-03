import re
content = '54cgjvekkhfewljevn'
content = re.sub('\d+', '', content)    # 把数字替换成空字符
print(content)