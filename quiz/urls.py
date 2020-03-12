"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import login, take_quiz, instructions, finish

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', login, name='login'),
    path('quiz/?P<user_id>', take_quiz, name='take_quiz'),  #takes user_id as parameter instead of using session or cookies
    path('instructions/?P<user_id>', instructions, name='instructions'),
    path('finish/', finish, name='finish'),
]

urlpatterns += staticfiles_urlpatterns()

# urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)