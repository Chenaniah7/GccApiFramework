# -*-coding:utf-8-*-
from api.project_manage import ProjectManageApi
# from common.project_manage_function import ProjectFunction


class ApiRunner():
    def __init__(self, base_url, userId, token, **kwargs):
        self.base_url = base_url
        self.userId = userId
        self.token = token
        self.projectApi = ProjectManageApi(self.base_url, self.userId, self.token, **kwargs)
# a = Gcw (token=token)
# print (a.projectApi.get_project_record ().json())
