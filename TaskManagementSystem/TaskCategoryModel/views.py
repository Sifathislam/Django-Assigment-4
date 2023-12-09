from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_Category(request):
    if request.method == 'POST':
        add_Category_form = forms.CategoryForm(request.POST)
        if  add_Category_form.is_valid():
            add_Category_form.save()
            return redirect('add_Category')
    
    else:
        add_Category_form = forms.CategoryForm()


    return render(request, 'add_category.html',{'form':add_Category_form})