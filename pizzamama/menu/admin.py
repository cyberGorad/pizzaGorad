from django.contrib import admin

from .models import Pizza

class Affichier(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix')
    search_fields = ["nom"]


admin.site.register(Pizza, Affichier)



# Register your models here.
