import httpx
client = httpx.Client(http2=True)    #默认支持的是http1，，需要申明一下才支持http2
response = client.get('https://spa16.scrape.center/')
print(response.text)