# coding=utf-8
from django.shortcuts import render
from django.http import  HttpResponse
from . import models
import logging
import  json
from django.contrib.auth import authenticate

logger = logging.getLogger('stu')

#使用表单登录
def logins(request):
    username =request.POST.get('username','USERNAME')
    password = request.POST.get('password', 'PASSWORD')
    print ('asas')
    try:
        user= models.User.objects.get(username=username)
        if password == user.password:
            return render(request, 'user_main.html')
        else:
            return render(request, 'add_article.html')
    except:
        return render(request, 'add_article.html')

#使用ajax登录
def login_ajax(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = models.User.objects.get(username=username)
            if password == user.password:
                return HttpResponse(1)
            else:
                return HttpResponse(2)
        except:
            return HttpResponse(3)


#进入用户注册界面
def register(request):
    return  render(request,'register.html')

#进入用户注册界面
def register(request):
    return  render(request,'register.html')

#使用表单注册用户信息
def register_user_info(request):
    username = request.POST.get('username','USERNAME')
    password = request.POST.get('password', 'PASSWORD')
    user=models.User.objects.create(username=username,password=password)
    return  render(request,'register.html')

#使用ajax注册用户信息
def  ajax_register_info(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = models.User.objects.filter(username=username).first()
    if(user==None):
        user = models.User.objects.create(username=username, password=password)
        #需要判断
        return HttpResponse(1)

    else:
        return HttpResponse(2)







def index(request):
    articles=models.Article.objects.all()
    return render(request,'index.html',{'articles':articles})


def article_page(request,article_id):
    article =models.Article.objects.get(pk=article_id)
    return  render(request,'article_page.html',{'article':article})

def editor_page(request,article_id):
    if int(article_id)==0:
        return render(request, 'editor_page.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request,'editor_page.html',{'article':article})

def add_article(request):
    return render(request,'add_article.html')

def edit_action(request):
     title =request.POST.get('title','TITLE')
     content = request.POST.get('content','CONTENT')
     article_id =request.POST.get('article_id','0')
     if int(article_id)==0:
         models.Article.objects.create(title=title,content=content)
         articles = models.Article.objects.all()
         return render(request, 'index.html', {'articles': articles})
     else:
         article = models.Article.objects.get(pk=int(article_id))
         article.title=title
         article.content=content
         article.save()
         articles = models.Article.objects.all()
         return render(request, 'index.html', {'articles': articles})
         return render(request, 'index.html', {'articles': articles})


def login(request):
    return render(request,'login.html')


def user_main(request):
    return  render(request,'user_main.html')





def register_user_info(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user=models.User.objects.create(username=username,password=password)
    return  render(request,'register.html')

def loginss(request):
    username =request.POST.get('username','USERNAME')
    password = request.POST.get('password', 'PASSWORD')
    return HttpResponse(1)