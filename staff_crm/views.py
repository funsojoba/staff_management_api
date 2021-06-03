from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Welcome nigga')


# Create your views here.
