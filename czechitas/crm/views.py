from django.views.generic import ListView, DetailView
from django.shortcuts import render
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
