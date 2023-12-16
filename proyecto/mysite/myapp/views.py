from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'myapp/index.html')

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'myapp/registro.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'myapp/inicio_sesion_exitoso.html', {'username': username})
    return render(request, 'myapp/login.html')

def formulario(request):
    if request.method == 'POST':
        # Procesar el formulario
        return render(request, 'myapp/formulario_exitoso.html')
    return render(request, 'myapp/formulario.html')
