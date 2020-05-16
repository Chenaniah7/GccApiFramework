# -*- coding: utf-8 -*-
from api_runner import Gcw
from operation.operationYaml import OperationYaml


class Env:
    def __init__(self, token, userId,**kwargs):
        self.apiRunner = Gcw(token=token, userId=userId)

