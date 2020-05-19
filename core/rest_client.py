# -*-coding:utf-8-*-
import requests


class RestClient:

    def __init__(self,token, **kwargs):
        self.s = requests.Session()
        self.token = token
        self.s.headers = {"Authorization": token, "Content-Type": "application/json"}

    def get(self, url, **kwargs):
        return self.request(url, "get", **kwargs)

    def post(self, url, **kwargs):
        return self.request(url, "post", **kwargs)

    def put(self, url, **kwargs):
        return self.request(url, "put", **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "delete", **kwargs)

    def request(self, url, method_name, **kwargs):
        # url = self.base_url + url
        if method_name == "get":
            return self.s.get(url, **kwargs)
        if method_name == "post":
            return self.s.post(url, **kwargs)
        if method_name == "put":
            return self.s.put(url, **kwargs)
        if method_name == "delete":
            return self.s.delete(url, **kwargs)

