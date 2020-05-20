from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def help_page (request):
    return render(request, 'help/help.html')