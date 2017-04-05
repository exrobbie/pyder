"""
This module is for human
"""

import requests
from bs4 import BeautifulSoup


def get_content():
    """ Get content from 糗事百科"""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    response = requests.get('https://www.qiushibaike.com', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    divs = soup.find_all(class_='content')
    for div in divs:
        joke = div.span.get_text()
        print(joke)
        print('---------------')


get_content()
