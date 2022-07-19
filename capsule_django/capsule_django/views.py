import imp
from django.shortcuts import render

#---- return index.html file ----
def index(request):
    return render(request, 'index.html')