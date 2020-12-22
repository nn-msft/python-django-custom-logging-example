from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)
def homePageView(request):
    logger.log("Hello World Visited!")
    return render(request, 'home/index.html', {'msg':'Hello World'})

def helloPageView(request):
    logger.log("More Hello")
    return render(request,'home/hello2.html',{'msg':'More Hello'})

def jsonSample(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    logger.log("==========Inside Json Sample===========")
    logger.log(str(request.body))
    logger.log("==========Data Contents==============")
    logger.log(str(data))
    logger.log("=========Let's return===========")
    return JsonResponse(data)