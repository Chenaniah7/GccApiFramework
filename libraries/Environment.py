# -*- coding: utf-8 -*-
from api_runner import Gcw


class Env:
    def __init__(self, token, userId, base_url, **kwargs):
        self.apiRunner = Gcw(token=token, userId=userId, base_url=base_url)
