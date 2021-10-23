from django.contrib.auth import authenticate,logout, login
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from student_management_app.EmailBackEnd import EmailBackEnd

# Create your views here.
def showPage(request):
    return render(request, "demo.html")

def showLogin(request):
    return render(request, "login.html")
def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user != None:
            login(request,user)
            return HttpResponse("Email : "+request.POST.get("email")+"Password: "+request.POST.get("password"))
        else:
            messages.error(request, "Invalid login details")
            return HttpResponseRedirect("/admin_home")

def getUserDetails(request):
    if request.user != None:
        return HttpResponse("User : "+request.user.email+" usertype : "+request.user.user_type)
    else:
        return HttpResponse("You need to login first")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")