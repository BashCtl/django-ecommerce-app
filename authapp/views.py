from django.shortcuts import render, redirect

# Create your views here.


def signup(request):

    if request.method == 'POST':
        pass
    else:
        pass
    
    return render(request, 'authentication/signup.html')


def user_login(request):
    return render(request, 'authentication/login.html')

def user_logout(request):
    return redirect('user_login')
