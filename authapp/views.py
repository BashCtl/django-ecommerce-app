from django.shortcuts import render, redirect
from .forms import SingupForm

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = SingupForm()

    context = {'form': form}

    return render(request, 'authentication/signup.html', context)


def user_login(request):
    return render(request, 'authentication/login.html')


def user_logout(request):
    return redirect('user_login')
