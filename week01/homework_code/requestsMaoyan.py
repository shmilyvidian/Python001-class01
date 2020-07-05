
# 安装并使用 requests、bs4 库，
# 爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，
# 并以 UTF-8 字符集保存到 csv 格式的文件中。

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
url = 'https://maoyan.com/films?showType=3'
cookie = 'uuid_n_v=v1; uuid=0306B9A0BE8D11EAA547EB67E957F0B1C947AAB069204E879F55B848CE7D26CC; _csrf=bd94537db41edb53fa29a37e0cc0e43b8873c025fe42f2224299738b8f786c22; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593932345; _lxsdk_cuid=1731dc56f1cc8-0e5d20f39fba37-143e6257-1aeaa0-1731dc56f1dc8; _lxsdk=0306B9A0BE8D11EAA547EB67E957F0B1C947AAB069204E879F55B848CE7D26CC; mojo-uuid=847c84543574509caba930bf4c5094e6; mojo-session-id={"id":"c90a210de3b39df477a536a49e3b68a0","time":1593932345176}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593932372; mojo-trace-id=3; __mta=250960441.1593932345198.1593932367402.1593932371865.3; _lxsdk_s=1731dc56f1f-af0-f9f-e78%7C%7C6'

header = {
    "user-agent": user_agent,
    "Cookie": cookie
}

# 保存数据到csv


def save_to_csv(data, fileUrl):
    res = pd.DataFrame(data=data)
    res.to_csv(fileUrl, encoding='utf8', index=False, header=False)

# 获取前十个电影名称、类型和上映时间


def get_maoyan_movie(url):
    mylist = []
    movie_type = None
    movie_time = None

    response = requests.get(url, headers=header)
    bs_info = bs(response.text, 'html.parser')

    for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}, limit=10):
        move_name = tags.find('span', attrs={'class': 'name'}).text
        for i, div in enumerate(tags.find_all('div')):
            if i == 1:
                movie_type = div.contents[2].strip()
            if i == 3:
                movie_time = div.contents[2].strip()
        mylist += [move_name, movie_type, movie_time]
    return mylist


if __name__ == "__main__":
    result = get_maoyan_movie(url)
    save_to_csv(result, './maoyan.csv')
