"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""


from music1.models import Protein
import csv

def loadData():
    
   
    csv_filepathname = '/Users/nurith/KenCampbell/Final/xmysite/file.csv'
    dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
    i = 0
    for row in dataReader:
        if i > 0:
            print (row)
            print ('row[0]:'+row[0])
            print ('row[1]:'+row[1])
            print ('row[2]:'+row[2])
            print ('row[3]:'+row[3])
            print ('row[4]:'+row[4])
            print ('row[5]:'+row[5])
            print ('row[6]:'+row[6])
            print ('row[7]:'+row[7])
            print ('row[8]:'+row[8])


            protein = Protein()
            protein.protein_id = 'AA' + '%04d' %i
            protein.peptidedb_id = row[0]
            protein.uniprot_id = row[1]
            protein.endonet_link = row[2]
            protein.known_fragments = bool(row[3])
            protein.hormone = bool(row[4])
            protein.pro_peptide = bool(row[5])
            protein.transcript = bool(row[6])
            protein.peptide_name= row[7]
            protein.fasta=row[8]
            protein.save()

        
        i = i + 1

#loadData()

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

application = get_wsgi_application()


