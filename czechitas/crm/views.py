from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from . import models

class MujDruhyPohled(View):
    def get(self, request):
        return HttpResponse('Vítej v CRM systému Czechitas!')


class KontaktyView(ListView):
    model = models.Kontakt
    template_name = "crm/crm_kontakty.html"

class OrganizaceView(ListView):
    model = models.Organizace
    template_name = "crm/crm_organizace.html"
