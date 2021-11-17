import datetime
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render

from student_management_app.models import CustomUser
from student_management_app.models import Courses

def admin_home(request):
    return render(request,"hod_templates/main_content.html")

def add_staff(request):
    return render(request, "hod_templates/add_staff_template.html")

def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            user.staffs.address=address
            user.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect("/add_staff")
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect("/add_staff")

def add_course(request):
    return render(request,"hod_templates/add_course_template.html")

def add_course_save(request):
    if request.method != "POST":
        return HttpResponseRedirect("Method not allowed")
    else:
        course = request.POST.get("course")
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request,"Successfully added course")
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request,"Failed to add Course")
    
def add_student(request):
    courses = Courses.objects.all()
    return render(request,"hod_templates/add_student_template.html",{"courses":courses})

def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        course_id=request.POST.get("course")
        session_start=request.POST.get("session_start")
        session_end=request.POST.get("session_end")
        sex=request.POST.get("sex")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
            user.students.address=address
            course_obj=Courses.objects.get(id=course_id)
            user.students.course_id=course_obj
            user.students.session_start_year=session_start
            user.students.session_end_year=session_end
            user.students.gender=sex
            user.students.profile_pic=""
            #print(user.students.course_id)
            user.save()
            messages.success(request,"Successfully Added Student")
            return HttpResponseRedirect("/add_student")
        except:
           messages.error(request,"Failed to Add Student")
           return HttpResponseRedirect("/add_student")
