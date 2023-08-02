# 引入path
from django.urls import path
from . import views
# 正在部署的应用的名称
app_name = 'publication'

urlpatterns = [
    path('publication-list/', views.pb_list, name='pb_list'),
    # path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
]