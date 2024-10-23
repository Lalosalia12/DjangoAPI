from django.shortcuts import render

def home_views(request):
    template_name = "login.html"
    
    return render(request,template_name)