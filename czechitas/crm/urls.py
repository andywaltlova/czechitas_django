from django.urls import path

from . import views

urlpatterns = [
    path('', views.MujDruhyPohled.as_view(), name='home'),
    path('kontakty/', views.KontaktyView.as_view(), name='kontakty'),
    path('organizace/', views.OrganizaceView.as_view(), name='organizace'),
]
