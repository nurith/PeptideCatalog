
from django.conf.urls import url
#from music1 import views
#from music1.views import setrow
from music1 import views as music1_views
from django.views.generic import TemplateView

app_name= 'music1'

urlpatterns=[
             
             url(r'^$', music1_views.index, name='index'),
             url(r'^setrow/(?P<row>\w+)/$',music1_views.setrow, name='setrow'),
             url(r'^database/$',music1_views.database, name='database'),
             url(r'^contact/$',music1_views.contact, name='contact'),
             #url(r'^search/$',music1_views.search, name='search'),
             url(r'^search/(?P<search>\w+([-]?\w+)*)/$',music1_views.search, name='search'),
             url(r'^fasta/(?P<entry>\w+)/$', music1_views.fasta, name='entry'),
             #      url(r'^entry/(?P<entry>\w+)/$', music1_views.entry, name='entry'),
             url(r'^entry/(?P<entry>\w+)/$', music1_views.entry, name='entry'),
             url(r'^sortby/(?P<entry>\w+)/$', music1_views.sortby, name='entry'),
             ]
