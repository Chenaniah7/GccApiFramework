import pytest
import json
import requests
from libraries.Environment import Env
from common.operationYaml import OperationYaml

yam = OperationYaml()
url = yam.readYaml()['login']['url']
data = json.dumps (yam.readYaml ()['login']['data'])
headers= {"Content-Type": "application/json"}


@pytest.fixture(scope="function")
def env():
    s=requests.Session()
    # s.params.update({"userId": "6951fef6-ec1b-43d7-ac53-6c74d074be7d",
    #                  "sysProjectID": "9f3c0ca6-35cc-4337-af57-904bfc5b6a53"})
    login_data = json.dumps(yam.readYaml()['login']['data'])
    r = s.post(url=url, data=login_data, headers=headers)
    # print(r.json())
    token = r.json()['Data']['Token']
    userId = r.json()['Data']['User']['UserId']
    yield Env(token=token, userId=userId)



