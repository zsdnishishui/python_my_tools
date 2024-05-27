import requests

from crypto import ctx

username = input("用户名：")
password = input("密码：")
username = ctx.call('stringtoaesencrypt', username)
password = ctx.call('stringtoaesencrypt', password)
# 返回code
code = requests.post('******', {'submit': 'submit'}).json()['code']

# 登录
data = {'username': username,
        'password': password,
        'uplcyid': '1',
        'language': '0',
        'code': code,
        'submit': 'submit'}
r = requests.post('*****', data)
print(r.text)
