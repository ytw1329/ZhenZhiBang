import json
from django.shortcuts import render, redirect
from . import models
from django.db.models import Max,Sum
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from .models import User,activity,Canyu,activity3,Child,Childimg,Sum1,donate

def index (request):
    summ = Sum1.objects.all()
    shows = donate.objects.all()
    sum = donate.objects.aggregate(Sums=Sum("damount"))

    s = sum['Sums']
    print(s)
    port = Sum1()
    port.sum = s
    port.save()
    context = {
        'shows': shows,
        'summ': summ,
        'sums': sum,
    }
    return render(request,'myapp/index.html',context)


def application(request):
    return render(request,'myapp/application.html')

def login(request):
    return render(request,'myapp/login.html')

def logining(request):
    name=request.POST.get('name',None)
    password=request.POST.get('password',None)
    tel=request.POST.get('tel',None)
    user=User.objects.filter(name=name,password=password)
    if user:
        context={
            'info':"登录成功"
        }

        request.session['love_user']={"name":name,'password':password,'tel':tel}
        return render(request, 'myapp/success.html', context)
    else:
        context={
            'info':"登陆失败,请重新登录"
        }
        return render(request, 'myapp/defeat.html', context)


def zhuce(request):
    return render(request,'myapp/zhuce.html')

def zhuceok(request):
    return render(request,'myapp/zhuceok.html')

def activityok(request):
    return render(request,'myapp/activityok.html')


def ok(request):
    return render(request,'myapp/ok.html')


def zhuceing(request):
    name=request.POST.get('name',None)
    password=request.POST.get('password',None)
    tel=request.POST.get('tel',None)

    user=User()
    user.name=name
    user.password=password
    user.tel=tel
    user.save()

    context={
        'info':"注册成功"
    }
    return render(request, 'myapp/zhuceok.html', context)
    return render(request,'myapp/index.html',context)

def dologout(request):
    del request.session['love_user']
    context={
        'info':"成功退出"
    }
    return render(request, 'myapp/index.html', context)


def geren(request):
    return render(request,'myapp/geren.html')

def adddata(request):
    return render(request,'myapp/adddata.html')

def xiugai(request,id):
    # loves=User.objects.all()
    port = User.objects.get(id=id)
    context = {
        'id': port.id,
        'name': port.name,
        'password': port.password,
        'tel': port.tel,
    }
    return render(request,'myapp/xiugai.html',context)

def xiugaidata(request,id):
    port=User.objects.get(id=id)
    port.id=request.POST.get('id',None)
    port.name=request.POST.get('name',None)
    port.password=request.POST.get('password',None)
    port.tel=request.POST.get('tel',None)
    print(port.id)
    print(port.name)
    print(port.password)
    print(port.tel)
    port.save()
    return render(request, 'myapp/xiugaiok.html')



def findpage(request):
    name=request.POST.get('find1',None)
    ports=User.objects.get(name=name)
    # p=Paginator(ports,5)
    # if(pIndex<1):
    #     pIndex=1
    # if pIndex>p.num_pages:
    #     pIndex=p.num_pages
    # ulist = p.page(pIndex)
    # page_list=p.page_range
    context={
        'id':ports.id,
        'name':ports.name,
        'password':ports.password,
        'tel':ports.tel,
    }
    return render(request, 'myapp/findpage.html',context)

def findpage3(request):
    name=request.POST.get('find3',None)
    ports=Canyu.objects.filter(name__contains=name)
    # p=Paginator(ports,10)
    # if(pIndex<1):
    #     pIndex=1
    # if pIndex>p.num_pages:
    #     pIndex=p.num_pages
    # ulist = p.page(pIndex)
    # page_list=p.page_range
    context={
        'airports':ports,
        # 'pIndex': pIndex,
        # 'page_list':page_list
     }
    return render(request, 'myapp/findpage3.html',context)


def findpage2(request,pIndex=1):
    name=request.POST.get('find2',None)
    ports=Childimg.objects.filter(name__contains=name)
    p=Paginator(ports,5)
    if(pIndex<1):
        pIndex=1
    if pIndex>p.num_pages:
        pIndex=p.num_pages
    ulist = p.page(pIndex)
    page_list=p.page_range
    context={
        'childd':ulist,
        'pIndex': pIndex,
        'page_list':page_list
    }
    return render(request, 'myapp/findpage2.html',context)


def gohome(request):
    return render(request,'myapp/gohome.html')

def 罕见病(request):
    return render(request,'myapp/罕见病.html')

def 常见罕见病(request):
    return render(request,'myapp/常见罕见病.html')

def 相关政策(request):
    return render(request,'myapp/相关政策.html')


def showdata(request):
    activities=activity.objects.all()
    context={
        'activities':activities,
    }
    return render(request,'myapp/showdata.html',context)

def adddata(request):
    activities=activity.objects.all()
    context={
        'activities':activities,
    }
    return render(request,'myapp/adddata.html',context)


def showdata2(request,pIndex=1):
    act=Canyu.objects.all()
    p = Paginator(act, 10)
    if pIndex < 1:
        pIndex = 1
    if pIndex > p.num_pages:
        pIndex = p.num_pages
    ulist = p.page(pIndex)
    page_list = p.page_range
    context = {'act': ulist,
               'pIndex': pIndex,
               'page_list': page_list
               }
    return render(request, 'myapp/showdata2.html', context)


def childshow(request):
    childd=Childimg.objects.all()
    context = {
        'childd': childd,
    }
    # p = Paginator(childd, 10)
    # if pIndex < 1:
    #     pIndex = 1
    # if pIndex > p.num_pages:
    #     pIndex = p.num_pages
    # ulist = p.page(pIndex)
    # page_list = p.page_range
    # context = {'childd': ulist,
    #            'pIndex': pIndex,
    #            'page_list': page_list
    #            }
    return render(request, 'myapp/childshow.html',context)

def childshow2(request):
    childd=Childimg.objects.all()
    context = {
        'childd': childd,
    }
    # p = Paginator(childd, 10)
    # if pIndex < 1:
    #     pIndex = 1
    # if pIndex > p.num_pages:
    #     pIndex = p.num_pages
    # ulist = p.page(pIndex)
    # page_list = p.page_range
    # context = {'childd': ulist,
    #            'pIndex': pIndex,
    #            'page_list': page_list
    #            }
    return render(request, 'myapp/childshow2.html',context)

def child(request):
    all_images = models.Childimg.objects.all()
    # for i in all_images:
    #     print(i.img)
    return render(request, 'child.html', locals())

def upload(request):
    error = ''
    if request.method == 'POST':
        img = request.FILES.get('img')

        models.Testimg.objects.create(img=img)
        print(img)
            # return redirect('childshow')
    return render(request, 'myapp/upload.html', locals())



def delete(request,id):
    pk = Childimg.objects.get(id=id)
    pk.delete()

    return render(request,'myapp/deleteok.html')

def canyu(request):
    activities=Canyu.objects.all()
    context={
        'activities':activities,
    }
    return render(request, 'myapp/findpage3.html', context)

def insert(request):
    name=request.POST.get('name',None)
    sex = request.POST.get('sex', None)
    tel = request.POST.get('tel', None)
    title=request.POST.get('title',None)
    context=request.POST.get('context',None)
    time=request.POST.get('time',None)
    place=request.POST.get('place',None)
    Organizer=request.POST.get('Organizer',None)
    qualifications=request.POST.get('qualifications',None)


    port=Canyu()
    port.name=name
    port.sex = sex
    port.tel = tel
    port.title=title
    port.context=context
    port.time=time
    port.place=place
    port.Organizer=Organizer
    port.qualifications=qualifications

    port.save()
    return render(request, 'myapp/activityok.html')

def insertchild(request):
    img=request.POST.get('img',None)
    name=request.POST.get('name',None)
    sex=request.POST.get('title',None)
    birthday=request.POST.get('context',None)
    place=request.POST.get('time',None)
    time=request.POST.get('place',None)
    detaile=request.POST.get('Organizer',None)


    port=Childimg()
    port.img=img
    port.name=name
    port.sex=sex
    port.birthday=birthday
    port.place=place
    port.time=time
    port.detaile=detaile
    # print(port.img)
    # print(port.name)
    # print(port.sex)
    # print(port.birthday)
    # print(port.place)
    # print(port.time)
    # print(port.detaile)
    port.save()
    return render(request, 'myapp/childinsertOK.html')

def insert2(request):
    dproject=request.POST.get('dproject',None)
    damount=request.POST.get('damount',None)
    dname=request.POST.get('dname',None)
    dtel=request.POST.get('dtel',None)
    dtext=request.POST.get('dtext',None)
    dway=request.POST.get('dway',None)

    port=donate()
    port.dproject=dproject
    port.damount=damount
    port.dname=dname
    port.dtel=dtel
    port.dtext=dtext
    port.dway=dway
    port.save()
    return render(request,'myapp/juanzengok.html')
    # return render(request,'myapp/index.html')

def BAOmingchuancan(request,id):
    activity_=activity.objects.get(id=id)
    context={
        'title':activity_.title,
        'time':activity_.time,
        'context':activity_.context,
        'Organizer':activity_.Organizer,
        'qualifications':activity_.qualifications,
        'place':activity_.place
    }
    # print(['title'])
    return render(request,'myapp/BBAAOOMing.html',context)


def baomingdata(request,id):
    port = activity.objects.get(id=id)
    # port.name = request.POST.get('name', None)
    port.title = request.POST.get('title', None)
    port.context = request.POST.get('context', None)
    port.time = request.POST.get('time', None)
    port.place = request.POST.get('place', None)
    port.Organizer = request.POST.get('Organizer', None)
    port.qualifications = request.POST.get('qualifications', None)
    # port.sex=request.POST.get('sex',None)
    # port.tel = request.POST.get('tel', None)
    port.save()

    # print(port.title)
    # ports=Canyu()
    # ports.name = port.name
    # ports.title = port.title
    # ports.context = port.context
    # ports.time = port.time
    # ports.place = port.place
    # ports.Organizer = port.Organizer
    # ports.qualifications = port.qualifications
    # ports.sex = port.sex
    # ports.tel = port.tel
    # ports.save()

    return HttpResponse(port.title + '已报名成功')


def editdata(request,id):
    port=activity.objects.get(id=id)
    port.title = request.POST.get('title', None)
    port.context = request.POST.get('context', None)
    port.time = request.POST.get('time', None)
    port.place = request.POST.get('place', None)
    port.Organizer = request.POST.get('Organizer', None)
    port.qualifications = request.POST.get('qualifications', None)
    print(port.title)
    port.save()







def apply(request):
    title = request.POST.get('title', None)
    context = request.POST.get('context', None)
    time = request.POST.get('time', None)
    place = request.POST.get('place', None)
    Organizer = request.POST.get('Organizer', None)
    qualifications = request.POST.get('qualifications', None)
    state = '待审核'

    port = activity3()
    port.title = title
    port.context = context
    port.time = time
    port.place = place
    port.Organizer = Organizer
    port.qualifications = qualifications
    port.state = state
    port.save()
    return render(request,'myapp/applyok.html')




def geliewei(request):
    return render(request, 'myapp/geliewei.html')

def baikeqi(request):
    return render(request, 'myapp/baikeqi.html')

def chushengquexian(request):
    return render(request, 'myapp/chushengquexian.html')

def tomorrow(request):
    return render(request, 'myapp/tomorrow.html')

def money(request):
    return render(request, 'myapp/money.html')

def juanzengok(request):
    return render(request, 'myapp/juanzengok.html')

def jijinhui(request):
    return render(request, 'myapp/jijinhui.html')
def help(request):
    return render(request, 'myapp/help.html')


def applyok(request):
    return render(request,'myapp/applyok.html')