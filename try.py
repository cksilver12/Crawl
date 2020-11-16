import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

baseurl = 'https://section.blog.naver.com/Search/Post.nhn?pageNo=1&rangeType=ALL&orderBy=sim&keyword='
plusurl = input('검색어를 입력하세요')
url = baseurl + urllib.parse.quote_plus(plusurl)

html = urllib.request.urlopen(url).read
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='sh_blog_tilte')

for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()