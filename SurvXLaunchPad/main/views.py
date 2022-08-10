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

def launchedprojects(request):
    context={}
    return render(request, 'main/launchedprojects.html', context)

def launchnewprojects(request):
    context={}
    return render(request, 'main/launchnewprojects.html', context)
def upcomingprojects(request):
    context={}
    return render(request, 'main/upcomingprojects.html', context)
def aboutus(request):
    context={}
    return render(request, 'main/aboutus.html', context)