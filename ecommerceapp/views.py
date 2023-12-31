from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Product, ProductCategory

# Create your views here.


def index(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()

    context = {'products': products, 'categories': categories}
    return render(request, 'index.html', context)


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(
                request, 'We will contact you as soon as it can be possible, little motherfucker.')
            return redirect('contact')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)


def about(request):
    return render(request, 'about.html')
