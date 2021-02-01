import pytest
from test_requests.req_page.contract import Contract


class TestContract:
    def setup_class(self):
        self.contract = Contract()
        self.userid = "hello112233"
        self.name = "hellotiaozhan700"

    @pytest.mark.parametrize("corpid,corpsecret,result",
                             [(None, None, 0), ('xxx', None, 40013), (None, 'xxx', 40001)])
    def test_token(self, corpid, corpsecret, result):
        r = self.contract.get_token(corpid, corpsecret)
        assert r.get("errcode") == result

    def test_create(self):
        self.contract.create_member(userid=self.userid, name=self.name, mobile="13244445555", department=[1],
                                    alias="xxx")
        try:
            result = self.contract.find_member(userid=self.userid)
        finally:
            self.contract.delete_member(userid=self.userid)
        assert result["name"] == self.name

    def test_update(self):
        self.contract.create_member(userid=self.userid, name=self.name, mobile="13233335555", department=[1],
                                    alias="xxx")
        changed_mobile = "13988887777"
        self.contract.update_member(self.userid, self.name, changed_mobile)
        try:
            result = self.contract.find_member(self.userid)
        finally:
            self.contract.delete_member(self.userid)
        assert result["mobile"] == changed_mobile

    def test_delete(self):
        userid = "hello223344"
        name = "223344"
        self.contract.create_member(userid=userid, name=name, mobile="132555534345555", department=[1], alias="xxx")

        result = self.contract.delete_member(userid)

        assert result["errmsg"] == "deleted"
