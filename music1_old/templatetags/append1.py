# templatetags/tag_library.py
import re
from django import template

register = template.Library()

@register.filter(name='get_href1')
def get_href1(value):
    return '<a href="http://www.peptides.be/index.php?p=peptide&peptide=' + value + '" target="_blank">'+ value +'</a>'

@register.filter(name='get_href_endo')
def get_href_endo(value):
    return '<a href="http://endonet.bioinf.med.uni-goettingen.de/hormone/' + value + '" target="_blank">'+ value +'</a>'

