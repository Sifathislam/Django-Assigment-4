from django.shortcuts import render
from TaskModel.models import add_task
def home(request):
    data = add_task.objects.all()
    return render(request, 'home.html',{'data': data})
