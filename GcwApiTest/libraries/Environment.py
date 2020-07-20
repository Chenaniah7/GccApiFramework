# -*- coding: utf-8 -*-
from api_runner import ApiRunner


class Env:
    def __init__(self, base_url, **kwargs):
        self.apiRunner = ApiRunner(base_url)



