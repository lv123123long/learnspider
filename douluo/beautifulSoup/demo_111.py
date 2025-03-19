
from bs4 import BeautifulSoup
with open('1.html', 'r', encoding='utf-8') as f:
    html_str = f.read()


def clean_css_js(html):
    # soup = BeautifulSoup(html, 'html_parser')
    soup = BeautifulSoup(html, 'html.parser')
    for element in soup.select('style,script,svg,nav'):
        element.decompose()
    
    return str(soup)

    '''
    这段代码使用soup.select方法选择HTML文档中的所有<style>、<script>、<svg>和<nav>元素。
    然后，对每个选中的元素调用decompose方法，该方法将元素从文档树中移除。
    '''


clean_html = clean_css_js(html_str)

with open('2.html', 'w', encoding='utf-8') as f:
    f.write(clean_html)