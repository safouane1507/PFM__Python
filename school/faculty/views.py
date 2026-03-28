# faculty/views.py
from django.shortcuts import render, redirect
#from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('First test')  <- l'ancienne version
    #return render(request, 'Home/index.html')
    return render(request, 'authentification/login.html')
def dashboard(request):
    return render (request, 'students/student-dashboard.html')