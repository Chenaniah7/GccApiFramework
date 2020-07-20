import requests


class ProjectFunction:

    def login(self, account, password, **kwargs):
        # 登录
        login_session = requests.session ()
        headers = {"Content-Type": "application/json"}
        data = {'account': account, 'password': password}
        return login_session.post ('http://113.108.203.26:6242/Login/Login', json=data, headers=headers)

        # token = r.json()['Data']['Token']
        # userId = r.json()['Data']['User']['UserId']

    def userid_projectid(self, account, password, **kwargs):
        # 返回一个项目记录id
        r = self.login (account=account, password=password).json ()
        pyload = {
            "userId": r['Data']['User']['UserId'],
            "sysProjectID": "9f3c0ca6-35cc-4337-af57-904bfc5b6a53",
        }
        return pyload

    def change_type(self,data, headers, **kwargs):
        """
        把参数转换成form data数据
        :param: data:  要传的参数
        :param: boundary: boundary的值
        :param: headers: 包含boundary的头信息；如果boundary与headers同时存在以headers为准
        :return: str
        :rtype: str
        """
        # 从headers中提取boundary信息
        fd_val = str (headers["Content-Type"])
        fd_var = fd_val.split (";")[1].strip ()
        boundary = fd_val.split ("=")[1].strip ()
        # form-data格式定式
        jion_str = '--{}\r\nContent-Disposition: form-data; name="{}"\r\n\r\n{}\r\n'
        end_str = "--{}--".format (boundary)
        args_str = ""

        if not isinstance (data, dict):
            raise Exception ("multipart/form-data参数错误，data参数应为dict类型")
        for key, value in data.items ():
            args_str = args_str + jion_str.format (boundary, key, value)
        #
        args_str = args_str + end_str.format (boundary)
        args_str = args_str.replace ("\'", "\"")
        return args_str
