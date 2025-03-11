# pip install beautifulsoup4 requests
# 这行注释表明需要安装beautifulsoup4和requests库，可以使用pip命令进行安装

from bs4 import BeautifulSoup
# 从bs4模块导入BeautifulSoup类，用于解析HTML和XML文档

with open('index.html', 'r') as f:
    # 使用with语句打开名为'index.html'的文件，'r'表示读取模式
    # 'as f'表示将打开的文件对象赋值给变量f
    html_str = f.read()
    # 读取文件内容，并将其赋值给变量html_str

soup = BeautifulSoup(html_str, 'html.parser')
# 使用BeautifulSoup类解析html_str，指定解析器为'html.parser'
# 解析后的结果赋值给变量soup，soup是一个BeautifulSoup对象，包含了HTML文档的结构

print("1.soup.p", soup.p)
# 打印字符串"1.soup.p"和soup对象中的第一个<p>标签的内容
# soup.p表示获取soup对象中的第一个<p>标签，如果没有<p>标签则返回None
