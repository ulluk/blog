"""
URL configuration for blog project.

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
from posts.views import home, post_list_view, post_detail_view, post_create_view
from users.views import register_view, login_view, logout_view
from django.conf.urls.static import static
from django.conf import settings

users_patterns = [
    path('register/', register_view, name = 'register'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('posts/', post_list_view),
    path('posts/<int:post_id>', post_detail_view),
    path('posts/create', post_create_view)
] + users_patterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)