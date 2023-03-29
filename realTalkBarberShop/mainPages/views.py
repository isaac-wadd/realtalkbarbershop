
from django.shortcuts import render

def indexView(req):
    return render(req, 'mainPages/index.html')
