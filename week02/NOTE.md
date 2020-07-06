学习笔记
### 异常捕获
    - 所有内置的非系统退出的异常都派生自Exception类
    - 通过traceback可以追踪到错误
    - 异常也是一个类
        - 异常类把错误消息打包到一个对象
        - 然后根据该对象会自动查找调用栈
        - 直到运行系统找到明确声明如何处理这些类异常的位置
    - 所有的异常继承自BaseException
    - TraceBack显示了出错的位置，显示的顺序和异常对象传播的方向是相反的
    - 捕获异常可以使用try...except语法，支持多重异常处理
    - 常见异常类型主要有：
        - LookupError下的IndexError和KeyError
        - IOError
        - NameError
        - TypeError
        - AttributeError
        - ZeroDivisonError
    - 自定义一个异常注意是需要从Exception类去继承实现
    - pretty_errors 异常第三方库
### 安装mysql
    - https://dev.mysql.com/downloads/mysql/
    - 启动 `ser`
    - 查看mysql是否运行 `ps -ef | grep mysql`
    - mysql -u root -p
    - python连接mysql
        - 安装第三方插件 pip3 install pymysql
    - 一般操作流程
        - 创建连接 -》创建connection -》获取cursor -》CRUD -》关闭cursor -》关闭connection-》结束
    - show databases;
    - create database test;
### 模拟浏览器行为
    - useragent
        - from fake_useragent import UserAgent
    - cookie
    - webdrive
        - http://chromedriver.storage.googleapis.com/index.html