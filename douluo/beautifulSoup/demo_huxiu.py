from bs4 import BeautifulSoup

with open('huxiu.html', 'r', encoding='utf-8') as f:
    html_str = f.read()


soup = BeautifulSoup(html_str, 'html.parser')

# print(soup)

artical_list = soup.select('.article-item-wrap')
# print(artical_list)

for artical in artical_list:
    print(artical)
    print("------------------")
    print(artical.select('a')[0].get('href'))
    print("++++++++++++++++++")
    print(artical.select('.author-name')[0].text)
    tmp_dict = {
        "title": artical.select('h3')[0].text,
        "url": artical.select('a')[0].get('href'),
        "author": artical.select('.author-name')[0].text,
        "time": artical.select('.bottom-line__time')[0].text,
    }
    print(tmp_dict)
    break
