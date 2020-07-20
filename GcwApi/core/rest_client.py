# -*-coding:utf-8-*-
import requests


class RestClient:

    def __init__(self,base_url,**kwargs):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}

    def get(self, url, **kwargs):
        return self.request(url, "get", **kwargs)

    def post(self, url, **kwargs):
        return self.request(url, "post", **kwargs)

    def put(self, url, **kwargs):
        return self.request(url, "put", **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "delete", **kwargs)

    def request(self, url, method_name, **kwargs):
        url = self.base_url + url
        if method_name == "get":
            return self.session.get(url, **kwargs)
        if method_name == "post":
            return self.session.post(url, **kwargs)
        if method_name == "put":
            return self.session.put(url, **kwargs)
        if method_name == "delete":
            return self.session.delete(url, **kwargs)




