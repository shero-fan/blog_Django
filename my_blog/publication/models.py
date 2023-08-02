from django.db import models

# Create your models here.
# 导入内建的User模型。
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# timezone 用于处理时间相关事务。
from django.utils import timezone

# 博客文章数据模型
class PublicationPost(models.Model):
    # 文章作者。参数 on_delete 用于指定数据删除的方式
    img_file = models.ImageField(upload_to='publication/%Y%m%d/', blank=True, null=True)
    # 文章标题。models.CharField 为字符串字段，用于保存较短的字符串，比如标题
    title = models.CharField(max_length=100)

    # pb_author = ArrayField(models.CharField(max_length=50),size=12)
    # pb_author_url = ArrayField(models.CharField(max_length=50),size=12)
    # 文章正文。保存大量文本使用 TextField
    author = models.TextField()
    keywords = models.TextField()

    # 文章创建时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)
    journal = models.CharField(max_length=100)
    journal_url = models.CharField(max_length=100)
    # website = models.CharField(max_length=100)
    website_url = models.CharField(max_length=100)
    # paper = models.CharField(max_length=100)
    paper_file = models.FileField(upload_to="publication/%Y%m%d/", blank=True)

    # 文章更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间
    # updated = models.DateTimeField(auto_now=True)
    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
    	# ordering 指定模型返回的数据的排列顺序
    	# '-created' 表明数据应该以倒序排列
        ordering = ('-created',)

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
    	# return self.title 将文章标题返回
        return self.title
