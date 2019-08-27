from django.urls import path
from . import views

urlpatterns = [
    path('ping', views.ping, name='ping'),
    path('login', views.login, name='login'),
    path('marker/2/retrieve', views.get_markers, name='get-markers'),
    path('marker/2', views.create_marker, name='create-marker'),
    path('marker/<int:marker_id>/update', views.update_marker, name='update-marker'),
    path('marker/<int:marker_id>/delete', views.delete_marker, name='delete-marker'),
    path('marker/<int:marker_id>/description', views.add_description, name='add-description'),
    path('marker/upload', views.upload_image, name='upload-image'),
]