# -*- coding: utf-8 -*-
import pytest, os
from api.base import ProjectFunction
import allure_pytest, allure

account = 'xxx'
password = 'xxxxxxx'
obj = ProjectFunction ()
token = obj.login (account, password).json ()['Data']['Token']
headers = {
    "Authorization": token,
    "Content-Type": "application/json"
}
iD = obj.userid_projectid (account, password)


def test_save_project_record(env):
    # 测试保存项目记录
    pyload = {
        "userId": iD['userId'],
        "sysProjectID": iD['sysProjectID'],
        "RecordType": 240,
        "Remark": "this is a test message"
    }
    header = {"Content-Type": "multipart/form-data;"
                              "boundary"
                              "=--------------------------137982354432402379816339"}
    headers.update (header)
    r = env.apiRunner.projectApi.save_project_record (data=pyload, headers=headers)
    assert r.status_code == 200
    assert r.json ()['Code'] == 1, "Code should be 1 but actually is {}".format (r.json ()['Code'])


# def test_save_project_record_files(env):
#     # 测试保存项目记录（上传文件）
#     request_file = {'test_photo': ('photo', open ('D:\GCW\PycharmProject\GccApiFramework\files'), 'image/png')}
#     pyload = {
#         "userId": iD['userId'],
#         "sysProjectID": iD['sysProjectID'],
#         "RecordType": 240,
#         "Remark": "this is a test message",
#         "File": request_file,
#     }
#     header = {"Content-Type": "multipart/form-data;"
#                               "boundary"
#                               "=--------------------------137982354432402379816339"}
#     headers.update (header)
#     r = env.apiRunner.projectApi.save_project_record (account, password, data=pyload, headers=headers)
#     assert r.status_code == 200
#     assert r.json ()['Code'] == 1, "Code should be 1 but actually is {}".format (r.json ()['Code'])


def test_get_project_record(env):
    # 测试获取项目记录
    pyload = {
        "sysProjectID": iD['sysProjectID'],
        "RecordType": 4
    }
    r = env.apiRunner.projectApi.get_project_record (data=pyload, headers=headers)
    assert r.status_code == 200
    assert r.json ()['Code'] == 1, "Code should be 1 but actually is {}".format (r.json ()['Code'])


def test_save_project_dailly_plan(env):
    # 测试保存项目计划
    header = {"Content-Type": "multipart/form-data; "
                              "boundary"
                              "=--------------------------006127840766512240517173"}
    headers.update (header)
    pyload = {
        "userId": iD['userId'],
        "sysProjectID": iD['sysProjectID'],
        "Remark": "I just want to test this api, don't worry",
        "StartTime": "2020-7-15",
        "EndTime": "2020-7-18",
    }
    r = env.apiRunner.projectApi.save_project_daily_plan (data=pyload, headers=headers)
    assert r.status_code == 200
    assert r.json ()['Code'] == 1, 'Code should be 1 but actually is {}'.format (r.json ()['Code'])


def test_get_project_daily_plan(env):
    # 测试获取项目计划
    pyload = {"sysProjectID": iD['sysProjectID']}
    r = env.apiRunner.projectApi.get_project_dailly_plan(data=pyload, headers=headers)
    assert r.status_code == 200
    assert r.json ()['Code'] == 1, 'Code should be 1 but actually is {}'.format (r.json ()['Code'])


def test_get_project_examination_record(env):
    # "测试获取项目考核记录"
    pyload = {
        "sysProjectRecordID": iD['sysProjectID']
    }
    r = env.apiRunner.projectApi.get_project_examination_record (data=pyload, headers=headers)
    assert r.status_code == 200
    assert r.json ()['Code'] == 1, 'Code should be 1 but actually is {}'.format (r.json ()['Code'])


def test_change_project_status(env):
    # "测试编辑项目状态"
    pyload = {
        "userId": iD['userId'],
        "sysProjectID": iD['sysProjectID'],
        "ProjectStatus": "新项目"
    }
    r = env.apiRunner.projectApi.change_project_status (data=pyload, headers=headers)
    assert r.status_code == 200
    assert r.json ()['Code'] == 1, 'Code should be 1 but actually is {}'.format (r.json ()['Code'])


def test_get_project_list(env):
    # "测试获取项目列表"
    r = env.apiRunner.projectApi.get_project_list (headers=headers)
    assert r.status_code == 200
    assert r.json ()['Code'] == 1, 'Code should be 1 but actually is {}'.format (r.json ()['Code'])


if __name__ == '__main__':
    pytest.main(['-m smoke','--html=reports/report.html'])
