from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from . import models


class MujPrvniPohled(View):
    def get(self, request):
        return HttpResponse('Vítej na webu Czechitas!')


class KurzyView(ListView):
    model = models.Kurz
    template_name = "kurzy/kurzy_list.html"


class DetailKurzView(DetailView):
    model = models.Kurz
    template_name = "kurzy/detail_kurzu.html"
