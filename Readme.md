简介：  
框架分为两个文件夹：ApiContent和ApiTest  

ApiContent：  
  api：   封装好的接口，可以直接调用  
  common：存放一些框架得公共方法，如：将json数据转换成form-data等方法  
  core：  框架核心，封装了requests方法  
  data：  管理测试数据，暂时用yaml文件管理，后续会更新excel  
  operation：存放数据驱动的操作代码，暂时只使用到yaml，后续会更新operationExcel  

ApiTest：  
  libraries: 放一些公共库  
  reports： 存放测试报告，目前框架使用html报告  
  tests：   存放测试用例，可在此目录下直接执行用例  
  
  
  
框架会持续更新优化。。  
