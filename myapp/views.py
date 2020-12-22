from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)
def homePageView(request):
    logger.debug("Hello World Visited!")
    return render(request, 'home/index.html', {'msg':'Hello World'})

def helloPageView(request):
    logger.debug("More Hello")
    return render(request,'home/hello2.html',{'msg':'More Hello'})

def jsonSample(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)