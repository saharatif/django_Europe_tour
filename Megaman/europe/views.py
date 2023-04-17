from django.shortcuts import render
from django.http import HttpResponse
from .models import Trip


def index(request):
    context={"trips": Trip.objects.all()}
    # return HttpResponse('This is my Europe trip')
    return render(request, "trips/index.html", context)

# Create your views here. 
## MVT Structure
