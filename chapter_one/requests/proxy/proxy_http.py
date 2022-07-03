import requests
proxies = {
    'http': 'http://10.10.10.10:1080',
    'https': 'https://10.10.10.10:1080',
}
requests.get('https://www.baidu.com/', proxies=proxies)

proxies = {
    'https': 'http://user:password@10.10.10.10:1080/',
}
requests.get("https://www.baidu.com/", proxies=proxies)