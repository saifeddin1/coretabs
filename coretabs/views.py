from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi there !!")

def hello(request):
    query = request.GET.get('name')
    return  HttpResponse("Hi {}".format(query))