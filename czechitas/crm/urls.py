from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('kontakty/', views.KontaktyView.as_view(), name='kontakty'),
    path('kontakty/<int:pk>', views.DetailKontaktView.as_view(), name='detail_kontakt'),
    path('organizace/', views.OrganizaceView.as_view(), name='organizace'),
    path('organizace/<int:pk>', views.DetailOrganizaceView.as_view(), name='detail_organizace'),
]
