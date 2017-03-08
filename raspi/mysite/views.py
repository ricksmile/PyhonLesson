# coding: utf-8
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from dnsimple import DNSimple
from mysite import models, forms
from django.conf import settings

def index(request, pid=None, del_pass=None):

    messages.get_messages(request)

    template = get_template('index.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

@login_required
def dnsmanager(request):
    messages.get_messages(request)

    subdomains = models.Subdomain.objects.filter(user=request.user)
    if len(subdomains)>0:
        records_in_dnsimple = subdomain_in_dnsimple(subdomains[0].name)
        main_subdomain = subdomains[0].name

    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        new_subdomain = models.Subdomain(user=user)
        form = forms.SubdomainForm(request.POST, instance=new_subdomain)
        if form.is_valid():
            cleaned_info = form.cleaned_data
            if  models.Subdomain.objects.filter(name=cleaned_info['name']).exists():
                messages.add_message(request, messages.WARNING, "該網址已被申請了!")
                return redirect('/dnsmanager')
            else:
                form.save()
                messages.add_message(request, messages.SUCCESS, "網址申請成功!")
                return redirect('/dnsmanager')
    else:
        form = forms.SubdomainForm()

    template = get_template('dnsmanager.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

@login_required
def del_subdomain(request, subdomain):
    messages.get_messages(request)
    try:
        target = models.Subdomain.objects.get(user=request.user, name=subdomain)
        target.delete()
        dns = DNSimple(username=settings.DNSIMPLE_USERNAME, password=settings.DNSIMPLE_PASSWORD)    
        records_in_dnsimple = subdomain_in_dnsimple(subdomain)
        for rec in records_in_dnsimple:
            try:
                dns.delete_record('raspi.tw', rec['id'])
            except:
                messages.add_message(request, messages.WARNING, "和DNSimple連線有異常！")
                pass
        messages.add_message(request, messages.SUCCESS, "成功刪除所有的記錄！")
    except:
        messages.add_message(request, messages.WARNING, "記錄刪除失敗！")
        pass
    return redirect('/dnsmanager')

@login_required
def del_record(request, rec_id):
    messages.get_messages(request)
    try:
        dns = DNSimple(username=settings.DNSIMPLE_USERNAME, password=settings.DNSIMPLE_PASSWORD)    
        dns.delete_record('raspi.tw', rec_id)
        messages.add_message(request, messages.SUCCESS, "成功刪除記錄！")
    except:
        messages.add_message(request, messages.WARNING, "記錄刪除失敗！")
        pass
    return redirect('/dnsmanager')

@login_required
def add_record(request, subdomain):
    messages.get_messages(request)
    if request.method=='POST':
        content = request.POST.get('content')
        record_type = request.POST.get('record_type')
        try:
            dns = DNSimple(username=settings.DNSIMPLE_USERNAME, password=settings.DNSIMPLE_PASSWORD)
            dns.add_record('raspi.tw', { 'name':subdomain, 
                                         'record_type':record_type,
                                         'content':content})   
            messages.add_message(request, messages.SUCCESS, "新增記錄成功！")
        except:
            messages.add_message(request, messages.WARNING, "新增記錄失敗！")
            pass
    return redirect('/dnsmanager')    


def subdomain_in_dnsimple(subdomain):
    dns = DNSimple(username=settings.DNSIMPLE_USERNAME, password=settings.DNSIMPLE_PASSWORD)
    try:
        raspi_records = dns.records('raspi.tw')
    except:
        return None
    raspi_dns_records = list()
    for raspi_record in raspi_records:
        if raspi_record['record']['name'] == subdomain:
            t=dict()
            t['id'] = raspi_record['record']['id']
            t['name'] = raspi_record['record']['name']
            t['record_type'] = raspi_record['record']['record_type']
            t['content'] = raspi_record['record']['content']
            raspi_dns_records.append(t)
    return raspi_dns_records