file = open('a.txt', encoding='utf8')

try:
    data = file.read()
    print(data)
except Exception as e:
    print(e)
finally:
    file.close()

with open('a.txt', encoding='utf8') as file2:
    data = file2.read()
    print(data)