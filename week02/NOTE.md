学习笔记

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