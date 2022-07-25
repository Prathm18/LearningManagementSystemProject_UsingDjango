from django.db import router
from django.urls import path,include
from app_users import views
from rest_framework import routers
from .views import ContactSerializers, ContactViewSet

# app_name = 'app_users'
router = routers.DefaultRouter()
router.register(r'contact',ContactViewSet)

urlpatterns = [
    path('school/',include(router.urls)),
    path('',views.HomeView.as_view(),name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('contact/', views.ContactView.as_view(), name="contact"),

]


