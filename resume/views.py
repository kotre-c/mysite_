from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    user_info = UserInfo.objects.filter(user__username='admin').all()[0]
    skill_list = Skill.objects.filter(user__name=user_info.name).all()
    return render(request, 'index.html', {'user_info': user_info, 'skill_list': skill_list})


def resume(request):
    user_info = UserInfo.objects.filter(user__username='admin').all()[0]
    expeience_list = Experience.objects.filter(user__name=user_info.name).all()
    education_list = Education.objects.filter(user__name=user_info.name).all()
    return render(request, 'resume.html', {'user_info':user_info, 'expeience_list': expeience_list, 'education_list':education_list})


# 项目
def portfolio(request):
    project_list = Project.objects.filter(user__name='张三')
    return render(request, 'portfolio.html', {'project_list': project_list})


# 项目详情
def portfolio_detail(request, id):
    project_list = Project.objects.filter(pk=id)
    return render(request, 'portfolio_detail.html', {'project_list': project_list})


def contact(request):
    user_info = UserInfo.objects.filter(user__username='admin')[0]
    return render(request, 'contact.html', {'user_info': user_info})
