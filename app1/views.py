from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def add_view(request):
    form = EmployeeForm
    if request.method =="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data add")
    return render(request,"app1/add.html",{"form":form})

def show_view(request):
    obj = Employee.objects.all()
    return render(request,"app1/show.html",{"emp":obj})

def update_view(request,pk):
    obj = Employee.object.get(id=pk)
    form = EmployeeForm(instance=obj)
    if request.method == "POST":
        form = EmployeeForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/add.html",{"form":form})

def delete_view(request,pk):
    obj = Employee.object.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("/a1/sv/")
    return render(request, "app1/delete.html", {"obj":obj})
