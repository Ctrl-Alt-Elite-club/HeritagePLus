from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def app(request):
    return render(request,'app.html')

def report(request):
    return render(request,'report.html')

def reports(request,r_id):
    return render(request,'reports.html')

def reportsAll(request):
    return render(request,'reports.html')