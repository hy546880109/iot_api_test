# Api自动化测试项目

## 介绍：

此项目主要用于测试我公司的微服务架构的云平台接口，使用requests + python + uniitest集成自动化测试。扩展了第三方的HTMLTestRunner库，支持python3，并且里面集成的了发邮件功能，同时封装了部分公共方法以及支持数据驱动。（本公司的服务器部署在内网所以里面的案例无法正常跑通）
在此感谢作者虫师提供的测试报告库，附上原始地址：https://github.com/SeldomQA/HTMLTestRunner
我在其基础进行了汉化。需要汉化报告的直接下载我的项目包，否则请使用原作者的包。

## 项目路径

![](https://ftp.bmp.ovh/imgs/2020/12/a4720b715d5af489.png)

### 目录说明：

* common：公共方法目录

* config：配置文件目录

* lib：第三方库目录

* main：主程序执行目录

* report：测试报告生成目录

* test_case：测试用例目录

* test_data：测试数据存放目录

* __init__.py: python执行标识文件
### 成果展示：

![](https://ftp.bmp.ovh/imgs/2020/12/b52638d5912cdb51.png)



### 后续：

* 增加数据库操作
* 增加获取token
* 增加websocket协议
* 增加测试报告方法
* 用例入参关联数据库
* 测试用例优化
* 增加失败重试机制
* 增加邮件发送测试报告
* 增加日志打印
* 增加环境参数切换命令
