import requests
response = requests.get('https://ssr2.scrape.center/', verify=False)   # verify参数 是否验证ssl证书
print(response.status_code)