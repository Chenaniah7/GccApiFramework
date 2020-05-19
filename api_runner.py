# -*-coding:utf-8-*-
from api.project_manage_api.project_manage import ProjectManageApi
# from common.project_manage_function import ProjectFunction


class Gcw:
    def __init__(self, token, userId, base_url,**kwargs):
        self.projectApi = ProjectManageApi(token=token, userId=userId, base_url=base_url)



a = Gcw (token=token)
print (a.projectApi.get_project_record ().json())
