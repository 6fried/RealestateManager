from django.contrib import admin
from .models import Maison, Client, Locataire, Paiement

admin.site.register(Maison)
admin.site.register(Client)

class PaymentInline(admin.StackedInline):
    model = Paiement
    extra = 1

@admin.register(Locataire)
class CustomerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Informations Personnelles', {
			'fields': ('firstname', 'lastname',)
            }
        ),
        
    	('Informations sur la Chambre', {
			'fields': ('home', 'roomid',)
			}	
		),

		('Information sur le paiement', {
			'classes': ('collapse',),
			'fields': ('startdate',)
			}	
		),
	)
    
    inlines = [PaymentInline]