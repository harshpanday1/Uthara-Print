from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Blog Index")

def blog(request):
    return render(request, "index.html")
