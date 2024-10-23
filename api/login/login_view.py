from django.shortcuts import render

def login_views(request):
    template_name = "login.html"
    
    return render(request,template_name)
#view for register
def registrar_views(request):
    template_name = "registrar.html"
    
    return render(request,template_name)

#view for password olvidado
def recuperar_views(request):
    template_name = "recuperar.html"
    
    return render(request,template_name)