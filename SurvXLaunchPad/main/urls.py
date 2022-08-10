from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('projects', views.projects, name='projects'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('forum', views.forum, name='forum'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('launchedprojects', views.launchedprojects, name='launchedprojects'),
    path('upcomingprojects', views.upcomingprojects, name='upcomingprojects'),
    path('launchnewprojects', views.launchnewprojects, name='launchnewprojects'),
]