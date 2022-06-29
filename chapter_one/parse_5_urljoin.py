from urllib.parse import urljoin
print(urljoin('https://baidu.com', 'FAQ.html'))
print(urljoin('https://baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('https://baidu.com/about.htnl', 'https://cuiqingcai.com/FAQ.html'))

#第一个参数会提供 scheme netloc path   ,如果第二个链接不包含这三个参数，则会使用第一个链接的这三个参数
# 真正起作用的是第二个链接
