# 使用requests爬取豆瓣影评
import requests
# 从bs4库中引入BeautifulSoup包并重命名为bs
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
cookie = 'bid=NVPhkGhUnRM; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __yadk_uid=FJ40fVs0KQJcFITlX5oNE9WiLDbDcUJR; _pk_id.100001.4cf6=d16497aa2141114b.1593926695.1.1593926700.1593926695.; __utma=30149280.1196407893.1593926701.1593926701.1593926701.1; __utmb=30149280.0.10.1593926701; __utmc=30149280; __utmz=30149280.1593926701.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1096296934.1593926701.1593926701.1593926701.1; __utmb=223695111.0.10.1593926701; __utmc=223695111; __utmz=223695111.1593926701.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
header = {'user-agent': user_agent, 'Cookie': cookie}

myUrl = 'https://movie.douban.com/top250'

response = requests.get(myUrl, headers=header)
bs_info = bs(response.text, 'html.parser')

for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
    for atag in tags.find_all('a'):
        href = atag.get('href')
        text = atag.find('span',).text
        print(f'href: {href}, text:{text}')
