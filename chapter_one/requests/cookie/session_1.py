import requests
'''
requests.get('https://www.httpbin.org/cookies/set/number/123456789')    #设置了一个带有cookie的请求
r = requests.get('https://www.httpbin.org/cookies')  #  再次获取该请求，是否能拿到我们设置的cookie
print(r.text)        #  答案是：不能,,,,,,不是同一个session
'''
s = requests.Session()
s.get('https://www.httpbin.org/cookies/set/number/123456789')
r = s.get('https://www.httpbin.org/cookies')
print(r.text)   # 可以，是同一个session

