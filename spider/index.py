"""
This module is for human
"""

import requests
from bs4 import BeautifulSoup


# def get_content():
#     """ Get content from 糗事百科"""
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
#     response = requests.get('https://www.qiushibaike.com', headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     divs = soup.find_all(class_='content')
#     for div in divs:
#         joke = div.span.get_text()
#         print(joke)
#         print('---------------')
#
#
# get_content()

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.p);



