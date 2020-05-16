# -*-coding:utf-8-*-
from api.project_manage_api.project_manage import ProjectManageApi
# from common.project_manage_function import ProjectFunction


class Gcw:
    def __init__(self, token, userId, **kwargs):
        self.projectApi = ProjectManageApi(token=token,userId=userId)



# token = obj.get_userid_token ()['Data']['Token']
# a = Gcw (token=token)
# print (a.projectApi.get_project_record ().json())
