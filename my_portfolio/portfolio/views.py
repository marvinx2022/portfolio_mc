from django.shortcuts import render



def index(request):
    return render (request,'portfolio/index.html')


def footer(request):
    return render (request,'portfolio/footer.html')


def about(request):
    return render (request,'portfolio/about.html')


def education(request):
    return render (request,'portfolio/education.html')


def header(request):
    return render (request,'portfolio/header.html')


def projects(request):
    return render (request,'portfolio/projects.html')


def services(request):
    return render (request,'portfolio/services.html')


def stack(request):
    return render (request,'portfolio/stack.html')

def management(request):
    return render (request, 'portfolio/management.html')