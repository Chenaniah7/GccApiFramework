# -*- coding: utf-8 -*-
import pytest
import pytest_html
import html

from api_runner import Gcw


def test_save_project_record(env):
    r =env.apiRunner.projectApi.get_project_record()
    assert r.json()['Code'] == 1, "Code should be 1 but actually is {}".format (r.json ()['Code'])


def test_save_project_record_file(env):
    r = env.apiRunner.projectApi.save_project_record_file ()
    assert r.status_code == 200
    assert r.json()['Code'] == 1


def test_get_project_record(env):
    r = env.apiRunner.projectApi.get_project_record ()
    assert r.json()['Code'] == 1


def test_save_project_daily_plan(env):
    r = env.apiRunner.projectApi.save_project_daily_plan()
    assert r.status_code == 200


def test_get_project_daily_plan(env):
    r = env.apiRunner.projectApi.get_project_daily_plan()
    assert r.json()['Code'] == 1


def test_get_project_examination_record(env):
    r = env.apiRunner.projectApi.get_project_examination_record()
    assert r.json()['Code'] == 1


def test_change_peoject_status(env):
    r = env.apiRunner.projectApi.change_project_status()
    assert r.json()['Code'] == 1


def test_get_project_list(env):
    r = env.apiRunner.projectApi.get_project_list()
    assert r.json()['Code'] == 1


if __name__ == '__main__':
    pytest.main()