import pretty_errors

def a():
    return b()


def b():
    return c()


def c():
    return d()


def d():
    x = 0
    return 100/x


try:
    a()
except Exception as e:
    try:
        1/0
    except Exception as f:
        print(f'f{f}')
    print(f'e{e}')


print('-----')
