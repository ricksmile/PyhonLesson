# _*_ encoding:utf-8 _*_
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from mysite import models, forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def index(request, pid=None, del_pass=None):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    template = get_template('index.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

@login_required(login_url='/login')
def userinfo(request):
    if request.user.is_authenticated():
        username = request.user.username
        try:
            userinfo = User.objects.get(username=username)
        except:
            pass
    template = get_template('userinfo.html')
    html = template.render(locals())
    return HttpResponse(html)


def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name=request.POST['username'].strip()
            login_password=request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, '成功登入了')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, '帳號尚未啟用')
            else:
                messages.add_message(request, messages.WARNING, '登入失敗')
        else:
            messages.add_message(request, messages.INFO,'請檢查輸入的欄位內容')
    else:
        login_form = forms.LoginForm()

    template = get_template('login.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, "成功登出了")
    return redirect('/')

@login_required(login_url='/login/')
def posting(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
        
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            message = "您的訊息已儲存，要等管理者啟用後才看得到喔。"
            post_form.save()
            return HttpResponseRedirect('/list/')
        else:
            message = '如要張貼訊息，則每一個欄位都要填...'
    else:
        post_form = forms.PostForm()
        message = '如要張貼訊息，則每一個欄位都要填...'          

    template = get_template('post2db.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)

    return HttpResponse(html)

