import requests
r = requests.get('https://www.httpbin.org/get')
print(r.text, type(r.text))

data = {
    'name': 'germey',
    'age': '25'
}
r = requests.get('https://www.httpbin.org/get', params=data)
print(r.text)