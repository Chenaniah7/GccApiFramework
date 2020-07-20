# -*- coding: utf-8 -*-
import json
from core.rest_client import RestClient
from api.base import ProjectFunction

obj = ProjectFunction ()


class ProjectManageApi (RestClient):

    def save_project_record(self, data, headers, **kwargs):
        """保存项目记录，form-data格式不上传文件"""
        self.session.headers = headers
        form_data = obj.change_type (data=data, headers=headers)
        return self.post ('/Project/SaveProjectRecord', data=form_data)

    def get_project_record(self, data, headers, **kwargs):
        """获取项目记录"""
        self.session.headers = headers
        return self.post ('/Project/GetProjectRecord', data=data)

    def save_project_daily_plan(self, data, headers, **kwargs):
        """保存项目工作计划，form-data格式"""
        self.session.headers = headers
        form_data = obj.change_type(data=data, headers=headers)
        return self.post('/Project/SaveProjectDailyPlan', data=form_data, headers=headers)

    def get_project_dailly_plan(self, data, headers, **kwargs):
        """获取项目工作计划"""
        self.session.headers = headers
        return self.post('/Project/GetProjectDailyPlan', data=data)

    def get_project_examination_record(self, data, headers, **kwargs):
        """获取项目考核情况"""
        self.session.headers = headers
        return self.post('/Project/GetProjectExaminationRecord', data=data, headers=headers)

    def change_project_status(self, data, headers, **kwargs):
        """编辑项目状态"""
        self.session.headers = headers
        return self.post('/Project/ChangeProjectStatus', data=data, headers=headers)

    def get_project_list(self, headers, **kwargs):
        "获取项目列表"
        self.session.headers = headers
        return self.post('/ Project/ List',  headers=headers)





