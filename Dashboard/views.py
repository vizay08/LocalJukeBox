from django.shortcuts import render

# Create your views here.
def presentDashboard(request):
    return render(request,"dashboard.html")