from django.contrib import admin
from django.urls import path
from webapp import views  # assuming your app is webapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),

]
