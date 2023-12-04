from django.shortcuts import render
from django.http import HttpResponse
def about(req):
    return render(req, 'about.html')
