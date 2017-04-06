import requests
from bs4 import BeautifulSoup


def get_magnet(keyword):
    url = 'https://btso.pw/search/' + keyword
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN, zh; q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'AD_clic_b_POPUNDER=2; AD_adst_b_MD_T_728x90=1; AD_popa_b_POPUNDER=2; AD_exoc_b_POPUNDER=1; AD_gung_b_POPUNDER=1; AD_wwwp_b_POPUNDER=1; AD_adca_b_POPUNDER=1; AD_avme_b_POPUNDER=1; AD_wwwp_b_MD_T_728x90=1; AD_adst_b_POPUNDER=1; AD_adma_b_POPUNDER=1; AD_wav_b_MD_B_728x90=6; AD_jav_b_MD_T_728x90=3; AD_javu_b_MD_B_728x90=4; AD_javu_b_MD_T_728x90=5; AD_jav_b_SM_B_728x90=5; AD_javu_b_SM_B_728x90=3; AD_wav_b_SM_B_728x90=4; AD_wav_b_MD_T_728x90=3; AD_jav_b_MD_B_728x90=3; _ga=GA1.2.672568651.1477887573; AD_enterTime=1491447840; AD_adca_b_SM_T_728x90=0; AD_jav_b_SM_T_728x90=0; AD_javu_b_SM_T_728x90=0; AD_wav_b_SM_T_728x90=0; AD_wwwp_b_SM_T_728x90=0; AD_adst_b_SM_T_728x90=1',
        'Host': 'btso.pw',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    a_tags = soup.find(class_='data-list').find_all('a')
    for a in a_tags:
        print(a.get('href'))


get_magnet('rbd-770')
