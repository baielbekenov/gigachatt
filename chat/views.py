from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def index2(request, pk):
    return render(request, 'index.html')