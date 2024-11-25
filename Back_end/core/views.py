from django.shortcuts import render
from .models import Pages


def index(request):
    context = {}
    try:
        first_page = Pages.objects.get(name="landing_page_first_section")
        second_page = Pages.objects.get(name="landing_page_sec_section")
        context = {
            "first_page" : first_page,
            "second_page": second_page,
        }
    except:
        pass

    return render(request, 'pages/index.html', context)

def cart(request):

    return render(request, 'pages/cart.html')


def detail(request):
    return render(request, 'pages/detail.html') 


def auth(request):

    return render(request, 'pages/auth.html')


def store(request):
    return render(request, 'pages/categoriespage.html')

def test(request):
    return render(request, 'pages/test.html')