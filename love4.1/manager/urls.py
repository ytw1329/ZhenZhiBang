from django.urls import path, include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('guanli/Manageindex', views.Manageindex,name='Manageindex'),

    # path('', views.index0,name='index0'),
    path('guanli/Manageshowdata', views.Manageshowdata,name='Manageshowdata'),
    path('guanli/Manageadd', views.Manageadd,name='Manageadd'),
    path('insertuser', views.insertuser,name='insertuser'),
    path('Manageedit/<int:id>', views.Manageedit,name='Manageedit'),
    path('Manageedit_data/<int:id>', views.Manageedit_data,name='Manageedit_data'),
    path('Managedelet/<int:id>', views.Managedelet,name='Managedelet'),
    path('guanli/Managefinddata', views.Managefinddata,name='Managefinddata'),
    path('adminlogining', views.adminlogining,name='adminlogining'),
    path('admienlogin', views.adminlogin,name='adminlogin'),
    path('base',views.base,name='base'),
    path('admindologout', views.admindologout,name='admindologout'),#管理员退出

    path('guanli/Manageadddata', views.Manageadddata,name='Manageadddata'),#管理员发布活动界面路由
    path('Manageinsert', views.Manageinsert, name='Manageinsert'),#管理员发布活动
    path('guanli/ManageShenHe', views.ManageShenHe, name='ManageShenHe'),#管理员审核活动界面路由
    path('shenhesucces/<int:id>',views.shenhesucces,name='shenhesucces'),#管理员审核活动同意发布
    path('shenhefail/<int:id>',views.shenhefail,name='shenhefail'),#管理员审核活动同意发布
    path('guanli/upload',views.upload,name='upload'),
    path('loginok',views.loginok,name='loginok'),
    path('logoutok',views.logoutok,name='logoutok'),
    path('managerindex',views.managerindex,name='managerindex'),
    # path('ShenHe',views.ShenHe,name='ShenHe'),

]
