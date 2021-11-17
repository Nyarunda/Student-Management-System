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
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type=="2":
                return HttpResponse("Staff login")
            else:
                return HttpResponse("Student login")
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")