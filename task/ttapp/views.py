from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
from .models import Student

@csrf_exempt
def stude_get(request):
    get_student = Student.objects.all()
    context = get_student
    return HttpResponse(context)

@csrf_exempt
def student_post(request):
    if request.method == "POST":
        add_student = Student.objects.create(f_name = request.POST['f_name'],l_name = request.POST['l_name'])
        add_student.save()
        msg = "Student added"
        return HttpResponse(msg)
    else:
        msg = "Some error"
        return HttpResponse(msg)

@csrf_exempt
def student_update(request,id):
    get_student = Student.objects.get(id = id)
    if request.method == "POST":
        get_student.f_name = request.POST['f_name']
        get_student.l_name = request.POST['l_name']
        get_student.save()
        msg = "Student Updated"
        return HttpResponse(msg)
    else:
        msg = "Some error"
        return HttpResponse(msg)

@csrf_exempt
def student_delete(request,id):
    get_student = Student.objects.get(id = id)
    get_student.delete()
    msg = "Student_deleted"
    return HttpResponse(msg)
