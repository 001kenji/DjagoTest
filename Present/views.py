from django.shortcuts import render, HttpResponse
from django.template import loader
# Create your views here.
def Home(request):
    homepage = loader.get_template('index.html')
    
    return HttpResponse(homepage.render())

def User(request):
    userpage = loader.get_template('user.html')

    return HttpResponse(userpage.render())
    