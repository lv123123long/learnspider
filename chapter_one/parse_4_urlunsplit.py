from urllib.parse import urlunsplit
#和urlunparse类似，只不过这里规定了传入的参数必须是5
data = ['https', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))