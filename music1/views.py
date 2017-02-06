# coding: utf-8
from random import choice
from django.http import HttpResponse
from django.template import loader, Context

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django_tables2 import SingleTableView

try:
    from django.urls import reverse
except ImportError:
    # to keep backward (Django <= 1.9) compatibility
    from django.core.urlresolvers import reverse

from django_tables2 import RequestConfig, SingleTableView

from .models import Protein, ProteinFilter
from .forms import ProteinFilterFormHelper
from .tables import ProteinTable


class PagedFilteredTableView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'

    def get_queryset(self, **kwargs):
        qs = super(PagedFilteredTableView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs
    
    def get_table(self, **kwargs):
        table = super(PagedFilteredTableView, self).get_table()
        RequestConfig(self.request, paginate={'page': 1,
                      "per_page": self.paginate_by}).configure(table)
        return table
    
    def get_context_data(self, **kwargs):
        context = super(PagedFilteredTableView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        context['row'] = self.paginate_by
        return context

class ProteinTableView(PagedFilteredTableView):
    model = Protein
    table_class = ProteinTable
    template_name = 'music1/database.html'
    filter_class = ProteinFilter
    formhelper_class = ProteinFilterFormHelper

    def get_table(self, **kwargs):
        self.paginate_by = self.kwargs.get('row', 10)
        return super(ProteinTableView, self).get_table()

class SearchView(ProteinTableView):
    model = Protein
    table_class = ProteinTable
    filter_class = ProteinFilter
    formhelper_class = ProteinFilterFormHelper
    template_name = ('music1/search.html')

def index(request):
    t = loader.get_template('music1/index.html')
    c=Context()
    return HttpResponse(t.render(c))

def contact(request):
    t = loader.get_template('music1/contact.html')
    c=Context()
    return HttpResponse(t.render(c))

def contrib(request):
    t = loader.get_template('music1/contributors.html')
    c=Context()
    return HttpResponse(t.render(c))

def sequence(request,seq):
    protein_list = Protein.objects.get(protein_id=seq)
    t = loader.get_template('music1/fasta_seq.html')
    c=Context({'all_proteins': protein_list})
    return HttpResponse(t.render(c))

class ViewUni(RedirectView):
    def get(self, request, **kwargs):
        uniprot = self.kwargs.get('uni', None)
        protein_list = Protein.objects.get(pk=uniprot)
        self.url = 'http://www.uniprot.org/uniprot/%s' % (protein_list.uniprot_id)
        return super(ViewUni, self).get(request, **kwargs)

class ViewPeptideDB(RedirectView):
    def get(self, request, **kwargs):
        peptidedbid = self.kwargs.get('pepdb', None)
        protein_list = Protein.objects.get(pk=peptidedbid)
        self.url = 'http://www.peptides.be/index.php?p=peptide&peptide=%s' % (protein_list.peptidedb_id)
        return super(ViewPeptideDB, self).get(request, **kwargs)

class ViewEndo(RedirectView):
    def get(self, request, **kwargs):
        endoid = self.kwargs.get('endo', None)
        protein_list = Protein.objects.get(pk=endoid)
        self.url = 'http://endonet.bioinf.med.uni-goettingen.de/hormone/%s' % (protein_list.endonet_link)
        return super(ViewEndo, self).get(request, **kwargs)

def entry(request,entry):
    protein_list = Protein.objects.get(protein_id=entry)
    t = loader.get_template('music1/detail.html')
    c=Context({'protein_list': protein_list,'entry': entry,})
    return HttpResponse(t.render(c))
