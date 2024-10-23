from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_views(request):
    template_name = "login.html"
    
    # Verifica si el usuario ya está autenticado
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, template_name, {'error': 'Credenciales inválidas'})
    
    return render(request, template_name)


#view for register
def registrar_views(request):
    template_name = "registrar.html"
    
    return render(request,template_name)

#view for password olvidado
def recuperar_views(request):
    template_name = "recuperar.html"
    
    return render(request,template_name)

#view for salir view
def salir_view(request):
    logout(request)
    return redirect('login')