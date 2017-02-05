# templatetags/tag_library.py

from django import template

register = template.Library()

@register.filter()
def dosearch(protein, search):
    return search == protein.protein_id or search == protein.peptidedb_id or search == protein.uniprot_id or search == protein.endonet_link or search in protein.peptide_name

