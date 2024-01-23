from django.shortcuts import render, HttpResponse
from django.template import loader
# Create your views here.
def Home(request):
    homepage = loader.get_template('index.html')
    
    if request.method == 'POST':
        return HttpResponse(homepage.render())
    else :
        return HttpResponse('your sending a wrong request')

def User(request):
    userpage = loader.get_template('user.html')

    if request.method == 'POST':
        return HttpResponse(userpage.render())
    else :
        return HttpResponse('your sending a wrong request')
    