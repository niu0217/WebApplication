from django.contrib import admin

from .models import Topic, Entry

# 让Django通过管理网站管理模型
admin.site.register(Topic)
admin.site.register(Entry)
