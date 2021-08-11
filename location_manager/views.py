from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views import generic
from .models import Maison, Locataire, Client
import pdfkit

def index(request):
    return render(request, template_name='lcm/index.html', context={"subtitle":"Home"})

class ClientView(generic.ListView):
    model = Client
    context_object_name = 'owners'
    template_name = 'lcm/clients.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'Liste des Clients' 
        return context

class BuildingView(generic.ListView):
    model = Maison
    context_object_name = 'buildings'
    template_name = 'lcm/buildings.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'Maisons à Charge' 
        return context


class BuildingDetailView(generic.DetailView):
    model = Maison
    context_object_name = 'building'
    template_name = 'lcm/building_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['subtitle'] = 'Maison'
        return context

class CustomerDetailView(generic.DetailView):
    model = Locataire
    context_object_name = 'customer'
    template_name = 'lcm/customer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['subtitle'] = 'Locataire'
        return context

def render_pdf(request, pk):
    customer = get_object_or_404(Locataire, pk=pk)
    name = 'Point de paiement: %s %s' % (customer.lastname, customer.firstname)

    url = '%s/printpdf/%d' % (request.get_host(), pk)

    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdk.exe')
    pdf = pdfkit.from_url(url,'', configuration=config)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="%s.pdf"' % name
    return response

def renders_to_pdf(request, pk):
    customer = get_object_or_404(Locataire, pk=pk)
    return render(request, template_name='lcm/print.html', context={'customer':customer})