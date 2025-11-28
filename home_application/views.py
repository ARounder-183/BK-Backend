from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blueking.component.shortcuts import get_client_by_request


# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")

def get_biz_data(request):
    client = get_client_by_request(request)
    kwargs = {'bk_biz_id': 1}
    result = client.cc.list_biz_hosts(kwargs)
    return JsonResponse(result)