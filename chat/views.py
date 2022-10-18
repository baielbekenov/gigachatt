from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def index(request):
    return render(request, 'index.html')

<<<<<<< HEAD

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            print('POST')
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account created for' + user)

                return redirect('login')
            else:
                print(form.errors)
        else:
            form = UserRegisterForm()

        context = {'form': form}
        return render(request, 'register.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Имя пользователя или пароль не правильно!')

        context = {}
        return render(request, 'login.html', context)

def logoutpage(request):
    logout(request)
    return redirect('login')
=======
def index2(request, pk):
    return render(request, 'index.html')
>>>>>>> 9ed58853aef5197b880d5c1837bcfecdcf04e130
