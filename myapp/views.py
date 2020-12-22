from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)
def homePageView(request):
    logger.log(logging.INFO,"Hello World Visited!")
    return render(request, 'home/index.html', {'msg':'Hello World'})

def helloPageView(request):
    logger.log(logging.INFO,"More Hello")
    return render(request,'home/hello2.html',{'msg':'More Hello'})

def jsonSample(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    logger.log(logging.INFO,"==========Inside Json Sample===========")
    logger.log(logging.INFO,str(request.body))
    logger.log(logging.INFO,"==========Data Contents==============")
    logger.log(logging.INFO,str(data))
    logger.log(logging.INFO,"=========Let's return===========")
    return JsonResponse(data)