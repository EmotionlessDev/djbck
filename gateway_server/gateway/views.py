import requests
from django.http import JsonResponse


def handle(request):
    url = "http://localhost:8000/get2"
    response = requests.get(url)
    return JsonResponse(response.json())
