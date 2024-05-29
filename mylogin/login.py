import requests
import subprocess
from functools import partial
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
subprocess.Popen = partial(subprocess.Popen,startupinfo=startupinfo, encoding='utf-8')
import execjs
from crypto import ctx

def login(username, password, encryption=True):
    key = execjs.compile(requests.get('****').text)
    encrypt_config_key = key.eval('encrypt_config_key')
    encrypt_config_iv = key.eval('encrypt_config_iv')
    if encryption:
        username = ctx.call('stringtoaesencrypt', username, encrypt_config_key, encrypt_config_iv)
        password = ctx.call('stringtoaesencrypt', password, encrypt_config_key, encrypt_config_iv)
    # 返回code
    code = requests.post('***', {'submit': 'submit'}).json()['code']

    # 登录
    data = {'username': username,
            'password': password,
            'uplcyid': '1',
            'language': '0',
            'code': code,
            'submit': 'submit'}
    # print(data)
    r = requests.post('***', data)
    r.encoding = r.apparent_encoding
    if not r.text.startswith('0#'):
        with open('data.txt', 'w') as file:
            file.write(username + '\n')
            file.write(password + '\n')  # 添加换行符
        return '登陆成功'
    else:
        return r.text


def main():
    # 查询保存的用户名密码，如果没有的话让用户自己输入
    username, password = get_save()
    if username == '' or password == '':
        username = input("请输入用户名：")
        password = input("请输入密码：")
        print(login(username, password))
    else:
        print(login(username, password, False))
def get_save():
    username = ''
    password = ''
    try:
        with open('data.txt', 'r') as f:
            for i, line in enumerate(f.readlines()):
                if i == 0:
                    username = line.strip()
                elif i == 1:
                    password = line.strip()
    except FileNotFoundError:
        print("没有找到用户名密码，请手动输入")
    return username, password

if __name__ == '__main__':
    main()
    input("请按任意键退出！")

