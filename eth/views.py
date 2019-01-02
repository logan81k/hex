from time import sleep

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, ethereum")

