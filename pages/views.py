from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args,**kwargs):


    return render(request=request,template_name='home.html',context={})

def about_view(request, *args, **kwargs):

    my_context = {
        'my_text':'some random text',
        'my_number':8263910646,
        'my_list':['hi','this','is','a','list']
    }

    return render(request=request,template_name='about.html',context=my_context)
