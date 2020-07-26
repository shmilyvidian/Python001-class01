import os


res = os.fork()
res1 = os.fork()


if res == 0:
    print('son', os.getpid(), os.getppid())
else:
    print('father', os.getpid())
print(f'res1={res1},res={res}')
# 等于0的为子进程，getpid当前进程ID，getppid当前进程父进程ID