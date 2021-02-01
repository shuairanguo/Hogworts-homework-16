import pytest
import yaml


def assfunction(a, b):
    return a + b


def get_datas():
    with open("../data.yml") as f:
        datas = yaml.safe_load(f)
        add_datas = datas["datas"]
        add_ids = datas["myid"]
        return [add_datas,add_ids]



@pytest.mark.parametrize(
    "a,b,expected",
    get_datas()[0], ids=get_datas()[1]
)
def test_add(a, b, expected):
    assert assfunction(a, b) == expected


get_datas()
