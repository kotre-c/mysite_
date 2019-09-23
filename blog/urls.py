from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog),
    path('<int:id>', views.blog_detail),
]