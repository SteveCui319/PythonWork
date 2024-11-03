import time

global name, user

user = {
    'name': 'steve',
    'pwd': '0319'
}


def login():
    global name
    name = input("Username:")
    pwsd = input("Password:")
    if name != user['name'] and pwsd != user['pwd']:
        return False

    return name


count = 0
while not login():
    time.sleep(3)  # 暂停3秒
    print('Authentication failure')
    count += 1
    if count == 3:
        break

print(name + '@localhost:~$')
