from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


def inicio(request):
    return render(request, "Appboots/index.html")


def saludo(request):
    return HttpResponse("helloo")


def hora(request):
    now = datetime.now()
    formatted_time = now.strftime("%A %d-%m-%y %H:%M:%S")
    return HttpResponse(formatted_time)
