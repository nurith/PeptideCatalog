import crispy_forms
from django import forms
from crispy_forms.helper import FormHelper
from .models import Protein
from crispy_forms.layout import Layout, Field, Submit
from crispy_forms.bootstrap import TabHolder, Tab


class ProteinFilterFormHelper(FormHelper):
    form_method = 'GET'
    model = Protein
    form_tag = False
    layout = Layout(
                    Field('protein_id'),
                    Field('peptide_name'),
                    Field('uniprot_id'),
                    Submit('submit', 'Search')
                    )

