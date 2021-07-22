import  re

from django.shortcuts import redirect
from django.urls import reverse
class AdminLoginMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        path=request.path
        print(path)
        if re.match('^/guanli/',path):
            if request.session.get('guanliyuan_user','')=='':
                return redirect(reverse('adminlogin'))
        response=self.get_response(request)
        return response