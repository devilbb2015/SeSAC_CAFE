from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def start(request):
    return HttpResponse("<a href='main'>" +
                        "<button style=width:200px; height:50px; background:red;>" +
                        "index" +
                        "</button>" +
                        "</a>")