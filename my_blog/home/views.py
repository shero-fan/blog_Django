from django.shortcuts import render
from .models import HomePost
# Create your views here.

# 导入 HttpResponse 模块
from django.http import HttpResponse

# 视图函数
def home_page(request):
    # 取出所有博客文章
    articles = HomePost.objects.all()
    # 需要传递给模板（templates）的对象
    context = { 'home': articles }
    return render(request, 'home/homepage.html',context)