from django.contrib.auth.models import Permission, User
from django.db import models
import django_filters

class Protein(models.Model):
    protein_id = models.CharField(max_length=25, primary_key=True)
    peptidedb_id = models.CharField(max_length=250)
    uniprot_id= models.CharField(max_length=250)
    endonet_link = models.CharField(max_length=250)
    known_fragments= models.BooleanField(default=False)
    hormone = models.BooleanField(default=False)
    pro_peptide= models.BooleanField(default=False)
    transcript= models.BooleanField(default=False)
    peptide_name= models.CharField(max_length=250)
    fasta=models.TextField(default='')
    
    def __str__(self):
        return self.protein_id

    def search (self, pattern):
        return True
    
    def get_absolute_url(self):
            return 'entry/%s' % self.pk

class ProteinFilter(django_filters.FilterSet):
    peptide_name = django_filters.CharFilter(lookup_expr='contains')
    class Meta:
        model = Protein
        fields = {
            'protein_id': ['exact'],
            'peptide_name': ['contains'],
	    'uniprot_id': ['exact'],
}
