from django.urls import path
from .views import RunCode

urlpatterns = [
    path('',RunCode.as_view(),name="runcode"),

]
