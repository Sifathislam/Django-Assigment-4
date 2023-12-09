from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_Task(request):
    if request.method == 'POST':
        add_Task_form = forms.TaskForm(request.POST)
        if  add_Task_form.is_valid():
            add_Task_form.save()
            return redirect('homepage')
    
    else:
        add_Task_form = forms.TaskForm()


    return render(request, 'add_task.html',{'form':add_Task_form})




def edit_task(request, id):
    task = models.add_task.objects.get(pk=id) 
    task_form = forms.TaskForm(instance=task)
    # print(post.title)
    if request.method == 'POST': 
        task_form = forms.TaskForm(request.POST, instance=task) 
        if task_form.is_valid():
            task_form.save() 
            return redirect('homepage')

    return render(request, 'add_task.html', {'form' : task_form})

def delete_task(request, id):
    task = models.add_task.objects.get(pk=id) 
    task.delete()
    return redirect('homepage')