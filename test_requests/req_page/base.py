import requests
from requests import Session

class Base:
    def __init__(self):
        self.s = Session()
        self.corpid = 'wwc87b7e8fdb00d6b2'
        self.corpsecret = 'W8teDahCaZ7U0EFSEKTgPCVdRc60iB3Pyhk1l7KmTNo'
        self.s.params["access_token"] = self.get_token().get("access_token")

    def get_token(self,corpid=None,corpsecret=None):
        if corpid is None:
            corpid = self.corpid
        if corpsecret is None:
            corpsecret = self.corpsecret
        parms = {"corpid":corpid,"corpsecret":corpsecret}
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",params=parms)
        return r.json()
