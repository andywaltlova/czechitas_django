from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from . import models


class KurzyView(ListView):
    model = models.Kurz
    template_name = "kurzy/kurzy_list.html"


class DetailKurzView(DetailView):
    model = models.Kurz
    template_name = "kurzy/detail_kurzu.html"


class VytvorPrihlasku(CreateView):
    model = models.Prihlaska
    template_name = "kurzy/prihlaska/prihlaska.html"
    fields = ["email", "jmeno", "prijmeni", "motivace", "kurz"]
    success_url = reverse_lazy('potvrzeni_prihlasky')

    def form_valid(self, form):
        id_kurzu = self.kwargs['pk']
        kurz = models.Kurz.objects.get(pk=id_kurzu)
        form.instance.kurz = kurz
        return super().form_valid(form)


class PotvrzeniPrihlasky(TemplateView):
    template_name = "kurzy/prihlaska/potvrzeni.html"
