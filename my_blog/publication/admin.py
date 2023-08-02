from django.contrib import admin

# Register your models here.
from .models import PublicationPost

# 注册ArticlePost到admin中
admin.site.register(PublicationPost)