介绍
----
一个基于 django 开发的 blog 程序。特性包括：
 - 注册，登录，修改密码，退出
 - 浏览，发布，修改，删除Blog

依赖
----
1. Python: 2.7
2. django: 1.4
3. markdown: `https://github.com/waylan/Python-Markdown/`


安装步骤
--------
1. (可选)删除`yblog/yblog.db`数据库文件， 执行 `python manage.py syncdb` 重新同步sqlite3数据库。 如果不删除原来的数据库文件，默认用户`admin@gmail.com`,密码`admin`

2. 执行 `python manage.py runserver` 启动临时服务器

3. 使用 `http://127.0.0.1:8000` 访问


参考和引用项目
--------------
 - [djblog]()
 - [openparty]()
 - [markdown](https://github.com/waylan/Python-Markdown/)
 - [wmd]()
 
