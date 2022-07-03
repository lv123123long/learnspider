import requests
from requests.packages import urllib3
urllib3.disable_warnings()         # 忽略警告
response = requests.get('https://ssr2.scrape.center/', verify=False)
print(response.status_code)