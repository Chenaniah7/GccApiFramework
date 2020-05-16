# -*-coding:utf-8-*-
import os

class PublicFunction:

    def filepath(self, filedir, filename):
        base_url = os.path.dirname (os.path.dirname (__file__))

        '''
        :param filedir: 文件目录
        :param filename: 文件名称
        :return:绝对路径
        '''
        return os.path.join (base_url, filedir, filename)

    @staticmethod
    def change_type(data,headers):
        """
        form data
        :param: data:  {"req":{"cno":"18990876","flag":"Y"},"ts":1,"sig":1,"v": 2.0}
        :param: boundary: boundary的值
        :param: headers: 包含boundary的头信息；如果boundary与headers同时存在以headers为准
        :return: str
        :rtype: str
        """
        # 从headers中提取boundary信息
        fd_val = str(headers["Content-Type"])
        fd_var = fd_val.split(";")[1].strip()
        boundary = fd_val.split("=")[1].strip()
        #
        # print('ffff'+fd_var)
        # print('bbb'+boundary)
        # form-data格式定式
        jion_str = '--{}\r\nContent-Disposition: form-data; name="{}"\r\n\r\n{}\r\n'
        end_str = "--{}--".format(boundary)
        args_str = ""

        if not isinstance(data, dict):
            raise Exception("multipart/form-data参数错误，data参数应为dict类型")
        for key, value in data.items ():
            args_str = args_str + jion_str.format(boundary, key, value)
#
        args_str = args_str + end_str.format(boundary)
        args_str = args_str.replace ("\'", "\"")
        return args_str


#
# headers = {"Content-Type": "multipart/form-data; boundary=--------------------------137982354432402379816339"}
#
#
# a=PublicFunction()
# print(a.change_type(data={}, headers=headers))
