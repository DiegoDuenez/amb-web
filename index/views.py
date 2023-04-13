from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    title = "DJANGO APP"
    return render(request, "index.html", {
        'title': title
    })
