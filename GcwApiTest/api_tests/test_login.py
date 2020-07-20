import pytest
from api.base import ProjectFunction
def test_login(env):
    r = env.apiRunner.login('test','zxc123456')
    assert r.json()['Code'] == 1, '登录失败'






    # assert r.json()['Code'] ==1

if __name__ == '__main__':
    pytest.main()