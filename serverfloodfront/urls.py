"""serverfloodfront URL Configuration

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
from server import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ping/', views.ping, name='ping'),
    path('api/login', views.login, name='login'),
    path('api/marker/2/retrieve', views.get_markers, name='get-markers'),
    path('api/marker/2', views.create_marker, name='create-marker'),
    path('api/marker/<int:marker_id>/update', views.update_marker, name='update-marker'),
    path('api/marker/<int:marker_id>/delete', views.delete_marker, name='delete-marker'),
    path('api/marker/<int:marker_id>/description', views.add_description, name='add-description'),
    path('api/marker/upload', views.upload_image, name='upload-image'),
]
