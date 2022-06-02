from django.urls import path

from . import views

app_name = 'calculator'
urlpatterns = [
path('', views.wrongcalc, name='wrongcalc'),
]

# just a test