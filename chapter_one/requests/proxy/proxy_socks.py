import requests
# pip install requests[socks]

proxies = {
    'http': 'socks5://user:password@host:port',
    'https': 'socks5://user:password@host:port'
}
requests.get("https://www.baidu.com", proxies=proxies)