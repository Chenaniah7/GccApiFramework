# -*- coding: utf-8 -*-
from api_runner import ApiRunner


class Env:
    def __init__(self, base_url, userId, token, **kwargs):
        self.apiRunner = ApiRunner(base_url, userId=userId, token=token)



