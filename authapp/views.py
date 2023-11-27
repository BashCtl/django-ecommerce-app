from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib import messages
from django.contrib.auth import logout
from django.views import View
from django.contrib.auth.models import User

from .forms import SingupForm
from .utils import generate_token, EmailSender

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email.lower()
            user.is_active = False
            user.save()
            EmailSender.send_activation_link(user)
            messages.success(
                request, 'Activate Your Account by the link in your email.')

            return redirect('login')
    else:
        form = SingupForm()

    context = {'form': form}

    return render(request, 'authentication/signup.html', context)


def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


class ActivateAccountView(View):

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as exc:
            user = None
        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.info(request, 'Account Activated Successfully.')
            return redirect('login')
        return render(request, 'authentication/activate_fail.html')
