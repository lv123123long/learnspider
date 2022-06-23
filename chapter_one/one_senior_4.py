import urllib.request, http.cookiejar

filename = 'cookie.txt'
#cookie = http.cookiejar.MozillaCookieJar(filename)  # Mozilla型的浏览器的cookie格式
cookie = http.cookiejar.LWPCookieJar(filename)    #LWP格式 （libwww.perl）
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

response = opener.open("https://www.baidu.com/")

cookie.save(ignore_discard=True, ignore_expires=True)