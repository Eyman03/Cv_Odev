from django.shortcuts import render

# Create your views here.

def initCv(request):
    return render(request, 'index.html')