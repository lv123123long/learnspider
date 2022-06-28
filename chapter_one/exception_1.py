from urllib import request,error
try:
    response = request.urlopen('https://cuiqingcai.com/404')
except error.URLError as e:
    print(e.reason)     #url不存在, url写错了，都可以