from urllib import request

# GET 方法
myUrl = 'https://movie.douban.com/top250'

resp = request.urlopen(myUrl)
print(resp.read().decode())