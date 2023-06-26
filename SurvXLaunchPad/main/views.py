from django.shortcuts import render


# Create your views here.
def home(request):
    context={}
    return render(request, 'main/home.html', context)

def projects(request):
    context={}
    return render(request, 'main/projects.html', context)
def forum(request):
    context={}
    return render(request, 'main/forum.html', context)

def dashboard(request):
    context={}
    return render(request, 'main/dashboard.html', context)

def portfolio(request):
    context={}
    return render(request, 'main/portfolio.html', context)

def products(request):
    context={}
    return render(request, 'main/products.html', context)

def daoproposals(request):
    context={}
    return render(request, 'main/daoproposals.html', context)
def marketplace(request):
    context={}
    return render(request, 'main/marketplace.html', context)
def aboutus(request):
    context={}
    return render(request, 'main/aboutus.html', context)
