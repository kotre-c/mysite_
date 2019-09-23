from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *

# Create your views here.


def blog(request):
    article_list = Article.objects.filter(user__username='admin', is_pub=True).all()
    return render(request, 'blog.html', {'article_list': article_list})


def blog_detail(request, id):
    article = Article.objects.get(pk=id)
    comment_list = Comment.objects.filter(article_id=id)

    if request.method == 'POST':
        article_id = id
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('message')
        Comment.objects.create(article_id=article_id ,name=name, email=email, text=text)
        return redirect('/blog/'+str(id))
    return render(request, 'blog_detail.html', {'article': article, 'comment_list': comment_list})