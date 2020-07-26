import os
import threading
import json


IPList = []
lock = threading.Lock()

# 1、ping指定IP判断主机是否存活


def ping_ip(ip):
    try:
        lock.acquire()
        output = os.popen(f'ping -c 1 {ip}').readlines()
        for w in output:
            if str(w).upper().find('TTL') >= 0:
                IPList.append(ip)
        lock.release()
    except Exception as e:
        print(e)


# 过滤不合法输入


def check_input(ip):
    forbidden_words = ['&', ';', '-', ' ', '||', '|']
    for i in forbidden_words:
        if i in host:
            print('输入不合法参数')
            exit()

#  保存json


def save_to_json(filename, data):
    with open(filename, 'w') as file_obj:
        json.dump(data, file_obj)


if __name__ == '__main__':
    host = input('请输入要检测的 IP : ')
    check_input(host)
    pre_ip = (host.split('.')[:-1])
    for i in range(1, 256):
        ip_address = ('.'.join(pre_ip)+'.'+str(i))
        t = threading.Thread(target=ping_ip, args=(ip_address,))
        t.start()

    current_path = os.path.abspath(os.path.dirname(__file__))
    save_to_json(current_path+'/ip.json', IPList)

    for ip in IPList:
        print(f'通过 {ip}')
