# coding: utf-8
import django_tables2 as tables
from django_tables2.utils import A
from .models import Protein

class ProteinTable(tables.Table):
    protein_id = tables.Column(linkify=('music1:entry',{'entry': tables.A('pk')}),attrs={'a': {'target': '_blank'}} )
    peptidedb_id = tables.Column(linkify=('music1:peptidedb_redirect',{'pepdb': A('pk')}), attrs={'a': {'target': '_blank'}})
    uniprot_id = tables.Column(linkify=('music1:uniprot_redirect',{'uni': A('pk')}), attrs={'a': {'target': '_blank'}})
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


