import httpx
response = httpx.get('https://www.httpbin.org/get')
print(response.status_code)
print(response.headers)  #字典
print(response.text) #字典