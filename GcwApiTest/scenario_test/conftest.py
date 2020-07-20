import pytest
from libraries.Environment import Env
from configparser import ConfigParser
from api.base import ProjectFunction

obj = ProjectFunction()

@pytest.fixture(scope="module")
def env():
    config = ConfigParser()
    config.read('../data/data.ini')
    base_url = config['test_env']['base_url']
    # token = obj.login()
    yield Env(base_url=base_url)



