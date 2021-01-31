import requests

'''
W8teDahCaZ7U0EFSEKTgPCVdRc60iB3Pyhk1l7KmTNo
'''


def test_contract():
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwc87b7e8fdb00d6b2&corpsecret=W8teDahCaZ7U0EFSEKTgPCVdRc60iB3Pyhk1l7KmTNo')
    print(r.json()['access_token'])


token = 'E1YjPw7gA-MLEZ9PCIdfT1FoAU4AIlLtFgdiHgJRRTB9_4PjhMym04Rb4mSz4iP3_JkzOk2U_LbXaSqzKZY44zLdKvktxGrJnPH6VftqJZ3jHgEnw5jZh1iSyXnG0KGyq7Xftw9QSIpo9PWMfq9ec_N1llwRxwGkK5vT_1MBES9Eku7SrI1yU7IddrpF3Eto_MW5b3tz_lea_ad_uWEUDQ'


def test_add_contract():
    data = {
        "userid": "zhangsan001",
        "name": "00221",
        "mobile":"+86 13381999999",
        "department":"4",
    }
    r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}', json=data)
    print(r.json())

def test_delete_contract():

    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=zhangsan001'
    r = requests.get(url=url)
    print(r.json())
