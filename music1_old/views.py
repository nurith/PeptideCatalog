from django.shortcuts import render
from .models import Protein
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader, Context



def setrow(request, row):
    contact_list = Protein.objects.all()
    paginator = Paginator(contact_list, row) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        proteins = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        proteins = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        proteins = paginator.page(paginator.num_pages)    
    t=loader.get_template('music1/database.html')
    return HttpResponse(t.render({"protein_list": proteins,'row':row}))

def index(request):
    t = loader.get_template('music1/index.html')
    c=Context()
    return HttpResponse(t.render(c))

def database(request):
    return setrow(request,25)


def search(request, search):
    protein_list = Protein.objects.all()
    t = loader.get_template('music1/database.html')
    c = Context({'protein_list': protein_list, 'row': 'All', 'search': search,})
    return HttpResponse(t.render(c))

def fasta(request,entry):
    all_proteins = Protein.objects.get(protein_id=entry)
    t = loader.get_template('music1/fasta_seq.html')
    c=Context({'all_proteins': all_proteins,'entry': entry,})
    return HttpResponse(t.render(c))

def entry(request,entry):
    protein_list = Protein.objects.get(protein_id=entry)
    t = loader.get_template('music1/detail.html')
    c=Context({'protein_list': protein_list,'entry': entry,})
    return HttpResponse(t.render(c))

def contact(request):
    t=loader.get_template('music1/contact.html')
    c=Context()
    return HttpResponse(t.render(c))

def sortby(request,entry):
    order = Protein._meta.ordering[0];
    if entry == order:
	Protein._meta.ordering[0] = '-' + entry;
    else:
	Protein._meta.ordering[0] = entry;
    return setrow(request,25)


"""
def setrow(request, row):
    protein_list = Protein.objects.all()
    t = loader.get_template('music1/database.html')
    c = Context({'protein_list': protein_list, 'row': row, 'search': '',})
    return HttpResponse(t.render(c))
def setrow(request,row):
       return HttpResponse("see value for row get passed as parameters to view=" +row)


"""
"""

class IndexView(generic.ListView):
model = Protein
template_name = "music1/index.html"
paginate_by = 10
request2= 0

def listing(request):
    request2=request
    contact_list = Protein.objects.all()
    paginator = Paginator(protein_list, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        proteins = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        proteins = paginator.page(paginator.num_pages)
    
    return render_to_response('index.html', {"proteins": proteins})

def get_context_data(self, **kwargs):
    request2=0
    # Call the base implementation first to get a context
    context = super(IndexView, self).get_context_data(**kwargs)
    # Add in a QuerySet of all the books
    context['rows'] = '2'
    return context




def table(request):
url(r'^processador/(?P<pk>[\w-]+)/$', ProcessadorUpdateView.as_view(), name='processador-detail'),
url(r'^software/(?P<pk>[\w-]+)/$', SoftwareUpdateView.as_view(), name='software-detail'),



    protein_list = Proteins.objects.all()
        t = loader.get_template('thefreemantrailapp/table.html')
        c = Context({'protein_list': proteins_list,})
        
        return HttpResponse(t.render(c))
"""
