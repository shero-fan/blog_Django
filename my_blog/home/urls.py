# 引入path
from django.urls import path
from . import views
# 正在部署的应用的名称
app_name = 'home'

urlpatterns = [
    path('home-page/', views.home_page, name='home_page'),
    # path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
]