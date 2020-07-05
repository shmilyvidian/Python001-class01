学习笔记
## 简单爬虫
### 相关知识
    - `requests` 第三方库获取网页内容
    - `urllib`
    - `BeautifulSoup`
    - `lxml`
    - `pandas`
### `requests`爬取豆瓣
    - 构造`headers header = { 'user-agent': xxx, Cookie: xxx }` 模拟浏览器操作
    - 使用  `requests.get(url, headers = header)`
    - 相关参数返回
        - `response.text`
        - `response.status_code`
### `urllib`爬虫
    - `from urllib import request`
    - `get` `request.urlopen(url)`
    - `post`  `request.urlopen(url, data=b'key=value',timeout=10)`
    - 返回内容 `resp.read().decode()`
### `bs4`提取网页内容
    - 引入 `from bs4 import BeautifulSoup as bs`
    - bs(response.text, 'html.parser')
    - find_all('element_name')
    - get('href')
    - find('element_name')
    - .text
### `lxml.etree`
    - 导人 from lxml import etree
    - selector = etree.HTML(repsonse.text)
    - selector.xpath('xpath')
### `panda`
    - DataFrame
    - to_csv(fileUrl, encoding='utf8', index=False, header=False)
### 翻页
    - `tuple(
    f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))`
### tips
    - `418` 认证失败被网页反爬虫没有添加请求头等信息，可能被反爬程序识别了，传入`header`和`cookie`
    - f f/format(): 格式化操作
    - 安装模块
        - `pip install [moduleName]`
        - `pip install -r requirements.txt`
    - 修改mac默认python版本 为python3
        ```
            vi ~/.bash_profile
            # 添加这一行
            alias python="/usr/bin/python3"
            source ~/.bash_profile
        ```
    - scrapy command not found
        ```
            ln -s  /Users/lishengfa/Library/Python/3.7/lib/python/site-packages/scrapy /usr/local/bin/scrapy
        ```
## Scrapy
   - Scrapy 架构官方文档介绍： https://docs.scrapy.org/en/latest/topics/architecture.html
   - 安装 pip3 install scrapy
   - 创建项目 scrapy startproject sipders
   - cd sipders && scrapy genspider movies  maoyan.com
   - scrapy crawl douban