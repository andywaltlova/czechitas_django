from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy
from . import models


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_kontakts = models.Kontakt.objects.all().count()
    num_orgs = models.Organizace.objects.all().count()

    context = {
        'num_contacts': num_kontakts,
        'num_organizations': num_orgs,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'crm/index.html', context=context)


class KontaktyView(ListView):
    model = models.Kontakt
    template_name = "crm/crm_kontakty.html"


class DetailKontaktView(DetailView):
    model = models.Kontakt
    template_name = "crm/detail_kontaktu.html"


class OrganizaceView(ListView):
    model = models.Organizace
    template_name = "crm/crm_organizace.html"


class DetailOrganizaceView(DetailView):
    model = models.Organizace
    template_name = "crm/detail_organizace.html"


class VytvorKontakt(CreateView):
    model = models.Kontakt
    template_name = "crm/kontakt/pridani.html"
    fields = ["jmeno", "prijmeni", "email", "datum_posledniho_kontaktu",
              "organizace"]
    success_url = reverse_lazy('potvrzeni_kontaktu')


class PotvrzeniKontaktu(TemplateView):
    template_name = "crm/kontakt/potvrzeni.html"


class VytvorOrganizaci(CreateView):
    model = models.Organizace
    template_name = "crm/organizace/pridani.html"
    fields = ["jmeno", "ico", "ulice", "mesto", "psc"]
    success_url = reverse_lazy('potvrzeni_organizace')


class PotvrzeniOrganizace(TemplateView):
    template_name = "crm/organizace/potvrzeni.html"







class VytvorKontaktOrganizaci(CreateView):
    model = models.Kontakt
    template_name = "crm/kontakt/pridani.html"
    fields = ["jmeno", "prijmeni", "email", "datum_posledniho_kontaktu"]
    success_url = reverse_lazy('potvrzeni_kontaktu')

    def form_valid(self, form):
        id_organizace = self.kwargs['pk']
        organizace = models.Organizace.objects.get(pk=id_organizace)
        form.instance.organizace = organizace
        return super().form_valid(form)
