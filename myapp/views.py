from django.http import HttpResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)
def homePageView(request):
    logger.debug("Hello World Visited!")
    return render(request, 'home/index.html', {'msg':'Hello World'})

def helloPageView(request):
    logger.debug("More Hello")
    return render(request,'home/hello2.html',{'msg':'More Hello'})
