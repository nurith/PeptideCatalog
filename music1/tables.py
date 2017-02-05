# coding: utf-8
import django_tables2 as tables
from django_tables2.utils import A
from .models import Protein

class ProteinTable(tables.Table):
    protein_id = tables.LinkColumn( attrs={'a': {'target': '_blank'}}, )
    peptidedb_id = tables.LinkColumn('music1:peptidedb_redirect',kwargs={'pepdb': A('pk')}, attrs={'a': {'target': '_blank'}})
    uniprot_id = tables.LinkColumn('music1:uniprot_redirect',kwargs={'uni': A('pk')}, attrs={'a': {'target': '_blank'}})
    endonet_link =tables.LinkColumn('music1:endonet_redirect',kwargs={'endo': A('pk')}, attrs={'a': {'target': '_blank'}})
    known_fragments=tables.BooleanColumn(yesno='Yes,')
    hormone =tables.BooleanColumn(yesno='Yes,')
    pro_peptide=tables.BooleanColumn(yesno='Yes,')
    transcript=tables.BooleanColumn(yesno='Yes,')
    peptide_name=tables.Column()
    fasta=tables.LinkColumn('music1:sequence',text='Show sequence', kwargs={'seq': A('pk')},attrs={'a': {'target': '_blank'}})

    class Meta:
        model = Protein
        attrs = {'class': 'paleblue'}


