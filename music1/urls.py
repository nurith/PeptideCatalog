# coding: utf-8
from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin
from django.views import static
from django.views.generic.base import RedirectView
from django_filters.views import FilterView

#from views import (index)
from music1 import views as music1_views
app_name= 'music1'

admin.autodiscover()

urlpatterns = [
    path('', music1_views.index, name='index'),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('search/',music1_views.SearchView.as_view(), name='search'),
    re_path('setrow/(?P<row>\w+)/$',music1_views.ProteinTableView.as_view(), name='setrow'),
    path('database/',music1_views.ProteinTableView.as_view(), name='database'),
    path('contact/',music1_views.contact, name='contact'),
    path('contributors/',music1_views.contrib, name='contributors'),
    re_path('database/entry/(?P<entry>\w+)/$',music1_views.entry, name='entry'),
    re_path('fasta/(?P<seq>\w+)/$', music1_views.sequence, name='sequence'),
    re_path('uniprot/(?P<uni>\w+)/$', music1_views.ViewUni.as_view(), name='uniprot_redirect'),
    re_path('peptidedb/(?P<pepdb>\w+)/$', music1_views.ViewPeptideDB.as_view(), name='peptidedb_redirect'),
    re_path('endonet/(?P<endo>\w+)/$', music1_views.ViewEndo.as_view(), name='endonet_redirect'),
    re_path('list/$', music1_views.filt_list),
]
