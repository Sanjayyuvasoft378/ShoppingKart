from django.urls import path
from . import views

urlpatterns = [
    path("regirtstion/",views.RegistrationAPI.as_view(),name='RegistrationAPI'),
]
