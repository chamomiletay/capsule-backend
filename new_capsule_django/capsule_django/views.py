#---- imports ----
import imp
from django.shortcuts import render

#---- views ----
#---- return index.html file ----
def index(request):
    return render(request, 'index.html')