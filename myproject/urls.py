"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('signup/', views.signup_user, name="signup_user"),
    path('signup2/', views.signup_user2, name="signup_user2"),
    path('login/', views.login_user, name="login_user"),
    path('changepass/', views.changepass, name="changepass"),
    path('changepass2/', views.changepass2, name="changepass2"),
    path('profilechange/', views.profilechange, name="profilechange"),
    path('profilechange2/', views.profilechange2, name="profilechange2"),
    path('profilechange3/', views.profilechange3, name="profilechange3"),
    path('admin/', admin.site.urls),
]
