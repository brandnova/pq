from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

from .forms import LoginForm

app_name = 'home'

urlpatterns = [
    path('about/', views.about, name='about' ),
    path('contact/', views.contact, name='contact' ),
    path('calculator/', views.gpa_cgpa_calculator, name='calculator' ),
    path('gpa-cgpa-result/', views.gpa_cgpa_result, name='gpa_cgpa_result'),
    path('services/', views.services, name='services' ),
    path('sample/', views.sample, name='sample'),
    path('departments/', views.departments, name='departments'),
    path('signup/', views.signup, name='signup'),
    # path('signin/', views.signin, name='signin'),

    path('signin/', auth_views.LoginView.as_view(template_name = 'signin.html', authentication_form = LoginForm), name='signin'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]