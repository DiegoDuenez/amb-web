from django.shortcuts import render
from django.http import HttpResponse
from docx.opc.constants import RELATIONSHIP_TYPE as RT
# Create your views here.

def index(request):

 
    links = [

            {
                "title":"Extraction, Purification, Structural Characteristics, Biological Activities and Pharmacological Applications of Acemannan, a Polysaccharide from Aloe vera: A Review",
                "url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6515206/"
            },
        
            {
                "title": "Chemical characterization of the immunomodulating polysaccharide of Aloe vera L",
                "url":"https://www.researchgate.net/publication/7939131_Chemical_characterisation_of_the_immunomodulating_polysaccharide_of_Aloe_vera_L"
            },

            {
                "title":"Oral administration of Aloe vera gel, anti-microbial and anti-inflammatory herbal remedy, stimulates cell-mediated immunity and antibody production in a mouse model",
                "url":"https://www.termedia.pl/Experimental-immunology-Oral-administration-of-Aloe-vera-gel-anti-microbial-and-anti-inflammatory-herbal-remedy-stimulates-cell-mediated-immunity-and-antibody-production-in-a-mouse-model,10,22985,1,1.html"
            },

            {
                "title":""
            }
    ]

    return render(request, "index.html", {
        'links': links
    })
