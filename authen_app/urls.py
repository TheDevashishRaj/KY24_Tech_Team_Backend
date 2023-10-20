from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('login/', views.login_user, name="Login"),
    path('signup/', views.signup_user, name="SignUp"),
    path('logout/', views.logout_user, name="Logout"),
]