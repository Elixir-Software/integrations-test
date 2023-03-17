from django.urls import path
from . import views

urlpatterns = [
    path("service/", views.ServiceView.as_view(), name="service_view"),
]
