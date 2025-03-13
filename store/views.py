# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Store!</h1>")



