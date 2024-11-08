from django.urls import path
from schedulo.api.views.base import HelloWorldView

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
]