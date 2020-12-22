from django.urls import path

from .views import homePageView, helloPageView,jsonSample

urlpatterns = [
    path('', homePageView, name='home'),
    path('hello',helloPageView),
    path('json1',jsonSample)
]