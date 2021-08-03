"""Location URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name='lcm'

urlpatterns = [
    path('', views.index, name='index'),
    path('clients', views.ClientView.as_view(), name = 'owners'),
    path('maisons', views.BuildingView.as_view(), name = 'buildings'),
    path('maisons/<int:pk>', views.BuildingDetailView.as_view(), name="building_detail"),
    path('locataires/', views.CustomerDetailView.as_view(), name='customers'),
    path('locataires/<int:pk>', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('print/<int:pk>', views.render_pdf, name="print"),
    path('printpdf/<int:pk>', views.renders_to_pdf, name="printpdf"),
]
