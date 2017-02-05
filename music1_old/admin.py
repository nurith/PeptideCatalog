from django.contrib import admin
from .models import Protein


class ProteinAdmin(admin.ModelAdmin):
    list_display=('protein_id','peptide_name')

admin.site.register(Protein, ProteinAdmin)

# Register your models here.
