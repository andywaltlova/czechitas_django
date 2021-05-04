from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('kontakty/', views.KontaktyView.as_view(), name='kontakty'),
    path('kontakty/<int:pk>', views.DetailKontaktView.as_view(), name='detail_kontakt'),
    path('organizace/', views.OrganizaceView.as_view(), name='organizace'),
    path('organizace/<int:pk>', views.DetailOrganizaceView.as_view(), name='detail_organizace'),
    path('kontakty/pridani', views.VytvorKontakt.as_view(), name='pridani_kontaktu'),
    path("organizace/<int:pk>/vytvor-kontakt", views.VytvorKontaktOrganizaci.as_view(), name="vytvor_kontakt_k_organizaci"),
    path('kontakty/potvrzeni', views.PotvrzeniKontaktu.as_view(), name='potvrzeni_kontaktu'),
]
