from django.db import models
from django.utils import timezone
import time
import datetime

class Client(models.Model):
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    
    def __str__(self):
        return ' '.join([self.firstname,self.lastname])

    def get_buildings(self):
        return Maison.objects.filter(owner=self)

    class Meta:
        db_table ='client'

class Maison(models.Model):
    name = models.CharField(max_length=80, blank=True)
    address = models.CharField(max_length=200)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="buildings")

    def __str__(self):
        return self.name

    def get_customers(self):
        return Locataire.objects.filter(home=self)

    class Meta:
        db_table ='maison'

class Locataire(models.Model):
    firstname = models.CharField(max_length=80, verbose_name='Prénoms')
    lastname = models.CharField(max_length=80, verbose_name='NOM')
    home = models.ForeignKey(Maison, on_delete=models.CASCADE, related_name="customers",verbose_name='Maison')
    roomid = models. PositiveIntegerField(default=0, verbose_name='N° de Chambre', unique=True)
    startdate = models.DateField(verbose_name="Date D'entrée", default=timezone.localdate)

    def get_payments(self):
        return Paiement.objects.filter(payer=self)

    def __str__(self):
        return ' '.join([self.firstname,self.lastname])

    class Meta:
        db_table ='locataire'

class Paiement(models.Model):
    date = models.DateField(auto_now_add=True)
    payer = models.ForeignKey(Locataire, on_delete=models.CASCADE, related_name='payment', verbose_name='Paiement',)
    paid = models.BooleanField(default=False, verbose_name='Payé')

    def __str__(self):
        return '%s Le %s' %(self.payer, self.date.strftime('%d/%m/%Y'))
    
    class Meta:
        db_table ='paiement'
