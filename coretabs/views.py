from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi there !!")

def hello(request, name):
    
    return  HttpResponse("Hi {}".format(name))