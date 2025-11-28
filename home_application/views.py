from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blueking.component.shortcuts import get_client_by_request


# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")

def get_biz_data(request):
    client = get_client_by_request(request)
    kwargs = {'page': {
        'start': 0,
        'limit': 20,
        'enable_count': True
    }}
    result = client.cc.search_business()
    return JsonResponse(result)