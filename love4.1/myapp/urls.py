from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    # path('index2',views.index2,name='index2'),
    path('application',views.application,name='application'),#用户申请活动跳转路由
    path('apply',views.apply,name='apply'),#用户申请活动具体方法
    path('login', views.login, name='login'),
    path('zhuceok', views.zhuceok, name='zhuceok'),
    path('logining', views.logining, name='logining'),
    path('activityok', views.activityok, name='activityok'),
    path('zhuce', views.zhuce, name='zhuce'),
    path('zhuceing', views.zhuceing, name='zhuceing'),
    path('dologout', views.dologout, name='dologout'),
    path('ok', views.ok, name='ok'),
    path('geren', views.geren, name='geren'),
    path('xiugai/<int:id>', views.xiugai, name='xiugai'),
    path('xiugaidata/<int:id>', views.xiugaidata, name='xiugaidata'),
    # path('zhongxin/<int:pIndex>', views.zhongxin, name='zhongxin'),
    path('findpage', views.findpage, name='findpage'),
    path('findpage3', views.findpage3, name='findpage3'),
    path('findpage2/<int:pIndex>', views.findpage2, name='findpage2'),
    path('gohome', views.gohome, name='gohome'),
    path('showdata', views.showdata, name='showdata'),
    path('showdata2/<int:pIndex>', views.showdata2, name='showdata2'),
    path('childshow', views.childshow, name='childshow'),
    path('childshow2', views.childshow2, name='childshow2'),
    path('canyu', views.canyu, name='canyu'),

    path('editdata/<int:id>', views.editdata, name='editdata'),
    path('insert',views.insert,name='insert'),
    path('insert2',views.insert2,name='insert2'),
    path('applyok',views.applyok,name='applyok'),
    path('insertchild',views.insertchild,name='insertchild'),
    path('love/adddata',views.adddata,name='adddata'),
    path('guanli/upload',views.upload,name='upload'),
    path('child',views.child,name='child'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('love/BAOmingchuancan/<int:id>',views.BAOmingchuancan,name='BAOmingchuancan'),
    path('罕见病',views.罕见病,name='罕见病'),
    path('常见罕见病',views.常见罕见病,name='常见罕见病'),
    path('相关政策',views.相关政策,name='相关政策'),
    path('geliewei',views.geliewei,name='geliewei'),
    path('baikeqi',views.baikeqi,name='baikeqi'),
    path('chushengquexian',views.chushengquexian,name='chushengquexian'),
    path('tomorrow',views.tomorrow,name='tomorrow'),
    path('money',views.money,name='money'),
    path('juanzengok',views.juanzengok,name='juanzengok'),
    path('jijinhui',views.jijinhui,name='jijinhui'),
    path('help',views.help,name='help'),


]