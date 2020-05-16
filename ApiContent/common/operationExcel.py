# #-*-coding:utf-8-*-# -*-coding:utf-8-*-
# import xlrd
# from common.pubilc import filepath
# from operation.operationYaml import OperationYaml
# import json
#
#
# class Excelvalues:
#     caseID = "测试用例ID"
#     caseModel = "模块"
#     caseName = "接口描述"
#     caseUrl = "请求地址"
#     casePre = "前置条件"
#     method = "请求方法"
#     paramsType = "请求参数类型"
#     params = "请求参数"
#     expect = "期望结果"
#     isRun = "是否运行"
#     headers = "请求头"
#     statusCode = "状态码"
#
#
# #
# #     @property
# #     def CaseID(self):
# #         return self.caseID
# #
# #     @property
# #     def Des(self):
# #         return self.des
# #
# #     @property
# #     def Url(self):
# #         return self.url
# #
# #     @property
# #     def Method(self):
# #         return self.method
# #
# #     @property
# #     def Data(self):
# #         return self.data
# #
# #     @property
# #     def Expect(self):
# #         return self.expect
# #
# #
# class OpretionExl(OperationYaml):
#     def getSheet(self):
#         pm = xlrd.open_workbook(filepath('data', 'api.xlsx'))
#         return pm.sheet_by_index(0)
#
#     #
#     #     @property
#     #     def getRow(self):
#     #         '''获取行数'''
#     #         return self.getSheet().nrows
#     #
#     #     @property
#     #     def getCols(self):
#     #         '''获取列数'''
#     #         return self.getSheet().ncols
#     #
#     #     def getvalue(self, row, cols):
#     #         return self.getSheet().cell_value(row, cols)
#     #
#     #     def getcaseID(self,row):
#     #         return self.getvalue(row=row,cols=Excelvalues().caseID)
#     #
#     #     def geturl(self,row):
#     #         return self.getvalue(row=row,cols=Excelvalues().Url)
#     #
#     #     def getmethod(self,row):
#     #         return self.getvalue(row=row,cols=Excelvalues().Method)
#     #
#     #     def getdata(self,row):
#     #         return self.getvalue(row=row,cols=Excelvalues().Data)
#     #
#     #     def getexcept(self,row):
#     #         return self.getvalue(row=row,cols=Excelvalues().Expect)
#     @property
#     def get_all_exceldata(self):
#         datas = []
#         title = self.getSheet().row_values(0)
#         for row in range(1, self.getSheet().nrows):
#             row_values = self.getSheet().row_values(row)
#             datas.append(dict(zip(title, row_values)))
#         return datas
#
#     def runs(self):
#         '''获取到可执行的测试用例'''
#         run_list = []
#         for item in self.get_all_exceldata:
#             isRun = item[Excelvalues.isRun]
#             if isRun == 'y':
#                 run_list.append(item)
#             else:
#                 pass
#         return run_list
#
#     def params(self):
#         '''请求参数为空做判断'''
#         for item in self.runs():
#             params = item[Excelvalues.params]
#             if (len(str(params).strip())) > 0:
#                 return json.loads(params)
#             else:
#                 pass
#
#
# if __name__ == '__main__':
#     obj = OpretionExl()
#     print(obj.params())
