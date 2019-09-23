from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index),            # 首页
    path('contact/', views.contact),        # 关于我
    path('portfolio/', views.portfolio),    # 档案
    path('resume/', views.resume),          # 简历
    path('portfolio/<int:id>', views.portfolio_detail)
]
