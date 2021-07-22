import re

from django.shortcuts import redirect
from django.urls import reverse

class AdminLoginMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        path=request.path
        if re.match('^/love/',path):
            if request.session.get('love_user','')=='':
                return redirect(reverse('login'))
        response=self.get_response(request)
        return response


