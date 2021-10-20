from django.shortcuts import render

# Create your views here.
def showPage(request):
    return render(request, "demo.html")

def login(request):
    return render(request, "login.html")
