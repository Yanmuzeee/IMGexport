import requests #引入requests库
from bs4 import BeautifulSoup #引入beautifulsoup
url="http://www.baidu.com"
response=requests.get(url)
print(response.text)


