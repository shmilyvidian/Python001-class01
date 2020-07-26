from datetime import datetime
with open('./a.txt', 'a+') as fs:
    print('jay chou', file=fs)

fp = open('./a.txt', 'a+')

print('come to there', file=fp)

fp.close()
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
