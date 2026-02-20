from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')
def hers(request):
    return render(request, 'hers.html')
def hert(request):
    return render(request, 'hert.html')
def thank(request):
    return render(request, 'thank.html')