from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages

# Create your views here.
@login_required(login_url="/login/")
def home(request):
    if request.method == 'POST':
        task_title = request.POST.get('task_title')
        task_desc = request.POST.get('desc')
        date_to_comp = request.POST.get('date_to_comp')
        AddNewTask.objects.create(
            user=request.user,
            task_title = task_title,
            task_desc = task_desc,
            date_to_comp = date_to_comp
        )

        return redirect('home')
    
    tasks = AddNewTask.objects.filter(user=request.user)  # Query all tasks from the model
    context = {'task': tasks}
    return render(request, 'index.html', context)

def delete_task(request,id):
    tasks = AddNewTask.objects.get(id = id)
    tasks.delete()
    return redirect('home')


def landing(request):
    return render(request, 'landing.html')

