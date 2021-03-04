from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import logging


logger = logging.getLogger('django')
def homePageView(request):
    
    logger.critical("Hello World Visited!")
    return render(request, 'home/index.html', {'msg':'Hello World Again04'})

def helloPageView(request):
    
    logger.critical("More Hello")
    return render(request,'home/hello2.html',{'msg':'More Hello'})

def jsonSample(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    logger.critical("==============jsonSample============")
    logger.critical("==========Inside Json Sample===========")
    logger.critical("=========="+str(request.body)+"===========")
    logger.critical("==========Data Contents==============")
    logger.critical("==========="+str(data)+"===============")
    logger.critical("=========Let's return===========")

    
    return JsonResponse(data)
