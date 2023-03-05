"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import *
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static



if settings.DEBUG: 

    urlpatterns = [
        path('admin/', admin.site.urls),
        path("admin-login/", AdminLoginView.as_view(), name="adminlogin"),
        path('',homepage, name = 'home'),
        path('register/', register, name='register'),
        path('login/', login_view, name='login'),
        path('crea_post/', CreaPost.as_view(), name='crea_post'),
        path('view_post/<int:post_id>/', view_post, name='view_post'),
        path("postslist/", AdminPostsListView.as_view(), name="adminpostslist"),
        path("logout/", LogoutView.as_view(), name="customerlogout"),
        path("logout/", logout, name="logout")    
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)