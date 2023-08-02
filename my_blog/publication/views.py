from django.shortcuts import render
# 导入 HttpResponse 模块
from django.http import HttpResponse
# 导入数据模型ArticlePost
from .models import PublicationPost

def pb_list(request):
    # 取出所有博客文章
    publications = PublicationPost.objects.all()
    # 需要传递给模板（templates）的对象
    context = { 'publications': publications }
    # render函数：载入模板，并返回context对象
    return render(request, 'publication/pb_list.html', context)