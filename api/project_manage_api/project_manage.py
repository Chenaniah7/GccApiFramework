# -*- coding: utf-8 -*-
import json
from common.operationYaml import OperationYaml
from common.pubilc import PublicFunction
# from common.project_manage_function import ProjectFunction
from core.rest_client import RestClient

yam = OperationYaml()
# obj = ProjectFunction()
pbc = PublicFunction()


class ProjectManageApi (RestClient):
    # userId = obj.get_userid_token()['Data']['User']['UserId']
    # auth = obj.get_userid_token()['Data']['Token']

    # def save_project_record(self, **kwargs):
    #     """保存项目记录，form-data格式不上传文件"""
    #     url = yam.readYaml()['save_project_record']['url']
    #     data = yam.readYaml()['save_project_record']['data']
    #     data['userId'] = self.userId
    #     headers = {"Authorization": self.token, "Content-Type": "multipart/form-data; "
    #                                                             "boundary"
    #                                                             "=--------------------------137982354432402379816339"}
    #     # print(headers)
    #     form_data = pbc.change_type (data=data, headers=headers)
    #     # print (dates)
    #     return self.post (url=url, data=form_data, headers=headers)
    #
    # def save_project_record_file(self, **kwargs):
    #     """ 保存项目记录，form-data格式，带文件上传 """
    #     url = yam.readYaml ()['save_project_record2']['url']
    #     data = yam.readYaml()['save_project_record']['data']
    #     headers = {"Authorization": self.token, "Content-Type": "multipart/form-data; "
    #                                                             "boundary"
    #                                                             "=--------------------------137982354432402379816339"}
    #     form_data = pbc.change_type (data=data, headers=headers)
    #     request_file = {'test_photo': ('photo', open('E:/ufly/test_photo.jpg'), 'image/jpeg')}
    #     # print(dates)
    #     return self.post (url=url, data=form_data, headers=headers)
    #
    # def get_project_record(self, **kwargs):
    #     """获取项目记录"""
    #     url = yam.readYaml()['get_project_record']['url']
    #     data = yam.readYaml()['get_project_record']['data']
    #     # data['userId'] = self.userId
    #     # headers = {"Authorization": self.auth, "Content-Type": "application/json"}
    #     data = json.dumps(data)
    #     return self.post(url=url, data=data)
    #
    # def save_project_daily_plan(self,**kwargs):
    #     """保存项目工作计划，form-data格式"""
    #     url = yam.readYaml()['save_project_daily_plan']['url']
    #     data =yam.readYaml()['save_project_daily_plan']['data']
    #     headers = {"Authorization": self.token, "Content-Type": "multipart/form-data; "
    #                                                             "boundary=--------------------------006127840766512240517173"}
    #     form_data = pbc.change_type(data=data, headers=headers)
    #     return self.post(url=url, data=form_data, headers=headers)
    #
    # def get_project_daily_plan(self,**kwargs):
    #     """获取项目工作计划"""
    #     data = json.dumps(yam.readYaml()['get_project_daily_plan']['data'])
    #     url = yam.readYaml()['get_project_daily_plan']['url']
    #     return self.post(url=url, data=data)
    #
    # def get_project_examination_record(self,**kwargs):
    #     """获取项目考核情况"""
    #     data = json.dumps(yam.readYaml()['get_project_examination_record']['data'])
    #     url = yam.readYaml()['get_project_examination_record']['url']
    #     return self.post(url=url, data=data)

    def change_project_status(self,**kwargs):
        """更改项目状态"""
        url = yam.readYaml()['change_project_status']['url']
        data = yam.readYaml()['change_project_status']['data']
        data['userId'] = self.userId
        data = json.dumps(data)
        return self.post(url=url, data=data)

    def get_project_list(self,**kwargs):
        """获取项目列表"""
        url = yam.readYaml()['get_project_list']['url']
        data = yam.readYaml()['get_project_list']['data']
        return self.post(url=url, data=data)





# a = ProjectManageApi ()
# print (a.get_project_record().json())
