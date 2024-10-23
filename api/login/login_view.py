from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def login_views(request):
    template_name = "login.html"

    # Verifica si el usuario ya está autenticado y activo
    if request.user.is_authenticated and request.user.is_active:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Verifica si el usuario autenticado es activo
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'El usuario no está activo')
        else:
            messages.error(request, 'Invalid login credentials')

    return render(request, template_name)

# Vista para registrar
def registrar_views(request):
    template_name = "registrar.html"
    
    if request.method == 'POST':
        # Obtención de los datos del formulario
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        # Verificar si las contraseñas coinciden
        if password != password_confirmation:
            messages.error(request, "Las contraseñas no coinciden")
            return render(request, template_name)

        # Verificar si el nombre de usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
            return render(request, template_name)

        # Verificar si el correo ya existe
        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo ya existe")
            return render(request, template_name)

        # Crear nuevo usuario
        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)  # Configura la contraseña de forma segura
        user.is_active = False  # Por defecto, los nuevos usuarios están inactivos
        user.save()

        # Mensaje de éxito y redirección al login
        messages.success(request, "Cuenta creada exitosamente. Por favor, espera a que un administrador active tu cuenta.")
        return redirect('login')

    # Retornar la plantilla en caso de GET o error
    return render(request, template_name)

# Vista para recuperar contraseña
def recuperar_views(request):
    template_name = "recuperar.html"
    
    return render(request, template_name)

# Vista para cerrar sesión
def salir_view(request):
    logout(request)
    return redirect('login')
