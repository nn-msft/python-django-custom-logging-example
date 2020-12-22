from django.http import HttpResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)
def homePageView(request):
    logger.error("Hello World Visited!")
    return render(request, 'home/index.html', {'msg':'Hello World'})
