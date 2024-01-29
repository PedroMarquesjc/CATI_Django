from django.urls import path
from . import views

urlpatterns = [
    path('calculo_pintura/',views.pintura_inicio),
    path('resultado_pintura/',views.pintura_inicio)
]
