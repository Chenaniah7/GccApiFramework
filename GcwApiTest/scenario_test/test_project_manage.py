# -*- coding: utf-8 -*-
import pytest, os
from api.base import ProjectFunction
import allure_pytest, allure

obj = ProjectFunction ()
sysProjectID = "a810562b-de90-4abe-9d9b-32f04370f562"


def test_save_project_record(env):
    # 测试保存项目记录
    data = {
        "sysProjectID": sysProjectID,
        "RecordType": 240,
        "Remark": "this is a test message"
    }
    headers = {"Content-Type": "multipart/form-data;"
                               "boundary"
                               "=--------------------------137982354432402379816339"}
    r = env.apiRunner.projectApi.save_project_record (data=data, headers=headers)
    sysProjectRecordID = r.json()['Data']['sysProjectRecordID']
    assert r.status_code == 200
    assert r.json ()['Code'] == 1, "Code should be 1 but actually is {}".format (r.json ()['Code'])
    return sysProjectRecordID


def test_get_project_record(env):
    # 测试获取项目记录
    data = {
        "sysProjectID": sysProjectID ,
        "RecordType": 4
    }
    r = env.apiRunner.projectApi.get_project_record (data=data)
    assert r.status_code == 200
    assert r.json ()['Code'] == 1, "Code should be 1 but actually is {}".format (r.json ()['Code'])


def test_save_project_dailly_plan(env):
    # 测试保存项目计划
    headers = {"Content-Type": "multipart/form-data; "
                               "boundary"
                               "=--------------------------006127840766512240517173"}
    data = {
        "sysProjectID": sysProjectID,
        "Remark": "I just want to test this api, don't worry",
        "StartTime": "2020-7-15",
        "EndTime": "2020-7-18",
    }
    r = env.apiRunner.projectApi.save_project_daily_plan (data=data, headers=headers)
    sysProjectDailyPlanID = r.json()['Data']['sysProjectDailyPlanID']
    assert r.status_code == 200
    assert r.json ()['Code'] == 1
    return sysProjectDailyPlanID


def test_get_project_daily_plan(env):
    # 测试获取项目计划
    data = {"sysProjectID": sysProjectID}
    r = env.apiRunner.projectApi.get_project_dailly_plan (data=data)
    assert r.status_code == 200
    assert r.json ()['Code'] == 1, 'Code should be 1 but actually is {}'.format (r.json ()['Code'])


def test_get_project_examination_record(env):
    # "测试获取项目考核记录"
    data = {
        "sysProjectID": sysProjectID
    }
    r = env.apiRunner.projectApi.get_project_examination_record (data=data)
    assert r.status_code == 200
    assert r.json ()['Code'] == 1, 'Code should be 1 but actually is {}'.format (r.json ()['Code'])


def test_change_project_status(env):
    # "测试编辑项目状态"
    data = {
        "sysProjectID": sysProjectID,
        "ProjectStatus": "新项目"
    }
    r = env.apiRunner.projectApi.change_project_status (data=data)
    assert r.status_code == 200
    assert r.json ()['Code'] == 1, 'Code should be 1 but actually is {}'.format (r.json ()['Code'])


def test_get_project_list(env):
    # "测试获取项目列表"
    r = env.apiRunner.projectApi.get_project_list ()
    assert r.status_code == 200
    assert r.json ()['Code'] == 1, 'Code should be 1 but actually is {}'.format (r.json ()['Code'])


if __name__ == '__main__':
    pytest.main (['-m', '-v',  '--html=../reports/report.html'])

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

    # }
