# -*- coding: utf-8 -*-
from api_runner import Gcw


class Env:
    def __init__(self, token, **kwargs):
        self.apiRunner = Gcw(token=token)

