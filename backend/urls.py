from django.conf.urls import url
from . import views

urlpatterns = [
    url('pages/', views.pages, name='pages'),
]