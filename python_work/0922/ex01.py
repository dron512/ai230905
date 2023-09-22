import requests
from bs4 import BeautifulSoup

# url = 'https://www.weather.go.kr/w/index.do'
url = 'http://silverfang.zc.bz/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

header_div = soup.find('div',id="header")
# print(header_div)

section_div = header_div.find('div',class_='section')
# print(section_div)
alist = section_div.select('a')
for a in alist:
    print(a.text)

at = section_div.select_one('a')
print(at)
