from django.shortcuts import render


from django.shortcuts import render

def admin_home(request):
    return render(request,"hod_templates/main_content.html")