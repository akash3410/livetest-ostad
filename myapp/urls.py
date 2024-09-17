from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home_page, name="home_page"),
    path('contact/add/', views.add_contact, name="add_contact"),
    path('contact/<int:pk>', views.contact_details, name="contact_details"),
    path('home/<int:pk>', views.delete_con, name="delete_con"),
    path('home/<int:pk>/update', views.update_contact, name="update_contact"),
]