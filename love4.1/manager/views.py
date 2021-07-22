from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myapp import models
from myapp.models import User,activity,activity3
from manager.models import AdminUser



def Manageindex(request):
    return render(request,'manager/index.html')


def Manageshowdata(request):
    love_data=User.objects.all()
    context={
        'datas':love_data
    }
    return render(request,'manager/showdata.html', context)


def Manageadd(request):

    return render(request,'manager/add.html')


def insertuser(request):
    name=request.POST.get('name',None)
    password=request.POST.get('password',None)
    tel=request.POST.get('tel',None)
    user=User()
    user.name=name
    user.password=password
    user.tel=tel
    user.save()
    print((name,password,tel))
    context={
        'info':'信息添加完毕'
    }
    return render(request, 'manager/info.html', context)


def Manageedit(request,id):
    user=User.objects.get(id=id)
    context={
        'id':user.id,
        'name':user.name,
        'password':user.password,
        'tel':user.tel
    }
    print(id)
    return render(request,'manager/edit.html',context)


def Manageedit_data(request,id):
    user=User.objects.get(id=id)
    print(user.name)
    user.name = request.POST.get('name', None)
    user.password = request.POST.get('password', None)
    user.tel = request.POST.get('tel', None)
    user.save()
    context={
        'info':'数据修改完毕'
    }
    return render(request, 'manager/info.html', context)


def Managedelet(request,id):
    user = User.objects.get(id=id)
    name=user.name
    user.delete()
    context={
        'info':name+"数据删除成功"
    }

    return render(request,'manager/info.html',context)


def Managefinddata(request):
    name=request.POST.get('find',None)
    user=User.objects.filter(name__contains=name)
    context={
        'datas':user
    }
    return render(request,'manager/showfind.html',context)

def base(request):
    return  render(request,'manager/base.html')

def adminlogin(request):
    return render(request,'manager/login.html')


def adminlogining(request):
    name=request.POST.get('name',None)
    password=request.POST.get('password',None)
    result_=AdminUser.objects.filter(name=name,password=password)
    if result_:
        request.session['guanliyuan_user']={'name':name,'password':password}
        context = {
            'info': "登陆成功"
        }
        return render(request,'manager/loginok.html')

    else:
        context = {
            'info': "登陆失败  "
        }
    return render(request,'manager/info.html',context)





def admindologout(request):
   del request.session['guanliyuan_user']
   return render(request,'myapp/logoutok.html')

def logoutok (request):
   return render(request,'manager/logoutok.html')


# def index0(request):
#     return render(request,'manager/index.html')





# def geren(request):
#     return render(request,'manager/geren.html')


def Manageadddata(request):
    return render(request, 'manager/adddata.html')


def Manageinsert(request):
    title=request.POST.get('title',None)
    context=request.POST.get('context',None)
    time=request.POST.get('time',None)
    place=request.POST.get('place',None)
    Organizer=request.POST.get('Organizer',None)
    qualifications=request.POST.get('qualifications',None)

    port=activity()
    port.title=title
    port.context=context
    port.time=time
    port.place=place
    port.Organizer=Organizer
    port.qualifications=qualifications
    port.save()
    return render(request,'manager/addok.html')

# def ShenHe(request):
#     return render(request,'manager/ShenHe.html')


def ManageShenHe(request,pIndex=1):
    activities = activity3.objects.all()
    p = Paginator(activities, 10)
    if pIndex < 1:
        pIndex = 1
    if pIndex > p.num_pages:
        pIndex = p.num_pages
    ulist = p.page(pIndex)
    page_list = p.page_range
    context = {'activities': ulist,
               'pIndex': pIndex,
               'page_list': page_list}
    return render(request, 'manager/ShenHe.html', context)

def shenhesucces(request,id):
    activity_ = activity3.objects.get(id=id)
    activity_.state='已通过'
    activity_.save()
    time=activity_.time
    context=activity_.context
    title=activity_.title
    place=activity_.place
    Organizer=activity_.Organizer
    qualifications=activity_.qualifications
    Activity=activity()
    Activity.title=title
    Activity.context=context
    Activity.time=time
    Activity.place=place
    Activity.Organizer=Organizer
    Activity.qualifications=qualifications
    Activity.save()
    activities = activity3.objects.all()
    context = {'activities': activities,
               }

    # statue_ = activity3.objects.filter(state='已通过')
    # context={
    #     'datas':statue_
    # }

    return render(request,'manager/ShenHe.html',context)


def shenhefail(request,id):
    activitydelete = activity3.objects.get(id=id)
    activities = activity3.objects.all()
    context = {'activities': activities,
               }
    activitydelete.delete()
    return render(request,'manager/ShenHe.html',context)

def upload(request):
    error = ''
    if request.method == 'POST':
        img = request.FILES.get('img')

        models.Testimg.objects.create(img=img)
        print(img)
            # return redirect('childshow')
    return render(request, 'myapp/upload.html', locals())

def loginok(request):
    return render(request, 'manager/loginok.html')

def managerindex(request):
    return render(request, 'manager/base.html')