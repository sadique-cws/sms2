from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Students


def homepage(Req):
    form = StudentForm(Req.POST or None)
    data = {
        "students" : Students.objects.all(),
        "form" : form
    }

    if Req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(homepage)
    
    return render(Req,"index.html",data)


def deleteStudent(r, id):
    student = Students.objects.get(pk=id)
    student.delete()
    return redirect(homepage)
