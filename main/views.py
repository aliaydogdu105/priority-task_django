from django.http import HttpResponse

def home(request):
    return HttpResponse('<center><h1 style="background-color:powderblue;">Welcome to Todo Api</h1></center>')