from django.contrib import admin
from django.urls import path
from farmapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('contact/', views.contact, name = 'contact'),
    path('testimonials/', views.testimonials, name = 'testimonials'),

]
