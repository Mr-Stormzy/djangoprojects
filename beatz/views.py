from django.shortcuts import render

def indexpage(request):
    return render(request, 'index.html')

def classpage(request):
    return render(request, 'classes.html')

def contactpage(request):
    return render(request, 'contact.html')

def shortcdspage(request):
    return render(request, 'shortcodes.html')

def showspage(request):
    return render(request, 'shows.html')

def trainspage(request):
    return render(request, 'trainings.html')