# WebApplication

## 1. Django入门

### 1.1 建立项目

#### 1.1.1 建立虚拟环境

虚拟环境：虚拟环境是系统的一个位置，你可以在其中安装包，并将这些包与其他Python包隔离起来。

先新建一个目录：`learning_log`

然后进入目录`learning_log`，并执行命令：

```bash
(venv)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  python -m venv ll_env     
(venv)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  ls
ll_env
```

此时创建了一个名为`ll_env`的虚拟环境。然后我们激活它：

```bash
(venv)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  source ll_env/bin/activate
(ll_env)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  
```

此时我们就进入到了虚拟环境中。

#### 1.1.2 安装Django

激活虚拟环境后，执行命令：

```bash
(ll_env)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  pip install --upgrade pip
(ll_env)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  pip install django
```

注意：Django仅在虚拟环境ll_env处于活动状态时才可以使用。

#### 1.1.3 在Django中创建项目

执行命令：

```bash
(ll_env)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  django-admin startproject ll_project .
(ll_env)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  ls
ll_env     ll_project manage.py
(ll_env)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  ls ll_project   
__init__.py asgi.py     settings.py urls.py     wsgi.py
(ll_env)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  
```

此时创建了一个名为`ll_project`的项目。其中自动创建了几个文件：

+ settings.py：指定Django如何与系统交互以及如何管理项目。
+ urls.py：告诉Django，应创建哪些网页来响应浏览器请求。
+ wsgi.py：帮组Django提供它创建的文件。

#### 1.1.4 创建数据库

执行命令：

```bash
(ll_env)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  python manage.py migrate
(ll_env)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  ls           
db.sqlite3 ll_env     ll_project manage.py

```

#### 1.1.5 查看项目

执行命令：

```bash
(ll_env)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  python manage.py runserver

```

![image-20231211111951260](README.assets/image-20231211111951260.png) 

### 1.2 创建应用程序

在前面打开的终端窗口运行着runserver，然后打开一个新终端窗口，执行命令：

```bash
(venv)  niu0217@niuM  ~/niuGithub/WebApplication/Dev   main ±  cd learning_log
(venv)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  source ll_env/bin/activate
(ll_env)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  python manage.py startapp learning_logs
(ll_env)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  ls
db.sqlite3    learning_logs ll_env        ll_project    manage.py
(ll_env)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  ls learning_logs
__init__.py admin.py    apps.py     migrations  models.py   tests.py    views.py
(ll_env)  niu0217@niuM  ~/niuGithub/WebApplication/Dev/learning_log   main ±  

```

命令`startapp appname`让Django创建应用程序所需的基础设施，其中重要的文件有：

+ models.py：定义要在应用程序中管理的数据
+ admin.py：
+ views.py：

#### 1.2.1 定义模型

修改文件：`/Dev/learning_log/learning_logs/models.py`

模型就是一个类，告诉Django如何处理应用程序中存储的数据。

```python
from django.db import models


# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""

    text = models.CharField(max_length=200)  # 用于存储标题、名称等小文本
    date_added = models.DateTimeField(auto_now_add=True)  # 获取当前时间

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
      
```

#### 1.2.2 激活模型

修改`/Dev/learning_log/ll_project/settings.py`，将其中的INSTALLED_APPS变量修改为如下形式：

```python
INSTALLED_APPS = [
    # 我的应用程序
    'learning_logs',

    # Django默认添加的应用程序
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

然后让Django修改数据库，使其能够存储与模型Topic、Entry相关的信息。执行命令：

```bash
```

