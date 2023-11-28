from multiprocessing import context
from django.shortcuts import render, redirect
from . forms import Employeeform
from . models import Employee

# Home page
def Home(request):
    form = Employeeform()

    if request.method == 'POST':
        form = Employeeform(request.POST)
        if form.is_valid():  # Check if the form is valid before saving
            form.save()
            return redirect('homepage')

    data= Employee.objects.all()
    context = {
        'form': form,
        'data': data,
    }
    return render(request, 'app1/index.html', context)

# Delete Funtionality
def Delete_Records(request, id):
    a = Employee.objects.get(pk=id)
    a.delete()
    return redirect('/')

# Update Funtionality
def Update_Records(request, id):
    if request.method=='POST':
        data = Employee.objects.get(pk=id)
        form = Employeeform(request.POST ,instance=data)
        if form.is_valid():
            form.save()
    else:    
        data = Employee.objects.get(pk=id)
        form = Employeeform(instance=data)
    context = {
        'form': form,
    }
    return render(request, 'app1/update.html',context)