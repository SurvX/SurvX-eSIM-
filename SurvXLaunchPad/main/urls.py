from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.products, name='products'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('forum', views.forum, name='forum'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('marketplace', views.marketplace, name='marketplace'),
    path('upcomingprojects', views.upcomingprojects, name='upcomingprojects'),
    path('daoproposals', views.daoproposals, name='daoproposals'),
]
