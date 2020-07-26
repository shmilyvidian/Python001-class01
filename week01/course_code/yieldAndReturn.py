def chain(num):
    for it in range(num):
        yield it


num = 5
y = chain(5)

# 推导式
mylist = []
for i in range(1, 11):
    if i > 5:
        mylist.append(i)

list_data = [i for i in range(1, 11) if i > 5]
myset = {i for i in 'HelloPython' if i not in 'on'}
print(f'list_data: {list_data}, mylist: {mylist}, myset: {myset}')
