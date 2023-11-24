from django.shortcuts import render, redirect
from .forms import SingupForm

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username=user.email.lower()
            user.save()
            return redirect('login')
    else:
        form = SingupForm()

    context = {'form': form}

    return render(request, 'authentication/signup.html', context)





def user_logout(request):
    return redirect('user_login')
