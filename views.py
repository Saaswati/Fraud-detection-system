from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(" this is nobo ka homepage ")
def about(request):
    return HttpResponse("this is the about page")
def services(request):
    return HttpResponse("this is the services page")
def contact(request):
    return HttpResponse("this is the contact page")
