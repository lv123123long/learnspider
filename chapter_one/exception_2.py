from urllib import request,error
try:
    response = request.urlopen('https://cuiqingcai.com/404')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')        #  url是正确的， 访问出错了

# URLError 是 HTTPError 的父类，可以先选择捕获子类的错误，再捕获父类的错误
try:
    response = request.urlopen('https://cuiqingcai.com/404')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except  error.URLError as e:
    print(e.reason)
else:
    print('Request Success!')
