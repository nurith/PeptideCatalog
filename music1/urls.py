# coding: utf-8
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views import static
from django.views.generic.base import RedirectView
from django_filters.views import FilterView

#from views import (index)
from music1 import views as music1_views
app_name= 'music1'

admin.autodiscover()

urlpatterns = [
    url(r'^$', music1_views.index, name='index'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^search/',music1_views.SearchView.as_view(), name='search'),
    url(r'^setrow/(?P<row>\w+)/$',music1_views.ProteinTableView.as_view(), name='setrow'),
    url(r'^database/$',music1_views.ProteinTableView.as_view(), name='database'),
    url(r'^contact/$',music1_views.contact, name='contact'),
    url(r'^contributors/$',music1_views.contrib, name='contributors'),
    url(r'^database/entry/(?P<entry>\w+)/$',music1_views.entry, name='entry'),
    url(r'^fasta/(?P<seq>\w+)/$', music1_views.sequence, name='sequence'),
    url(r'^uniprot/(?P<uni>\w+)/$', music1_views.ViewUni.as_view(), name='uniprot_redirect'),
    url(r'^peptidedb/(?P<pepdb>\w+)/$', music1_views.ViewPeptideDB.as_view(), name='peptidedb_redirect'),
    url(r'^endonet/(?P<endo>\w+)/$', music1_views.ViewEndo.as_view(), name='endonet_redirect'),
    url(r'^list/$', music1_views.filt_list),
]
