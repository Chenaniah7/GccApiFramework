import pytest
from libraries.Environment import Env
from configparser import ConfigParser
from api.base import ProjectFunction

obj = ProjectFunction()
account = 'test'
password = 'xxxxxxx'


@pytest.fixture(scope="module")
def env():
    config = ConfigParser()
    config.read('../data/data.ini')
    base_url = config['test_env']['base_url']
    r = obj.login(account=account, password=password)
    userId = r.json()['Data']['User']['UserId']
    token = r.json()['Data']['Token']
    yield Env(base_url=base_url, userId=userId, token=token)



