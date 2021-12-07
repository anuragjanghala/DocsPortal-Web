from django.urls import path
from portalapp import views


urlpatterns = [
    path('', views.index, name='landing-page'),
]
