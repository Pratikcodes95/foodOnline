from django.urls import path
from . import views
from .views import registeruser

urlpatterns = [
    path('registeruser/', views.registeruser,name='registeruser'),
]
