**STEP-1**
 
 Add the following code to settings.py file.
	 
import logging.handlers
 
LOGGING = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                     'standard': {
                     'format': '[%(levelname)s] %(asctime)s - %(name)s - %(message)s',
                     'datefmt' : "%d/%b/%Y %H:%M:%S"
                 },
          },
            'filters': 
            {
                'require_debug_false': 
                    {
                        '()': 'django.utils.log.RequireDebugFalse'
                    }
            },
            'handlers': 
            {
                'logfile': 
                    {
                        'class': 'logging.handlers.WatchedFileHandler',
                        'filename': '/home/site/wwwroot/app-log-1.log', 
                        'formatter': 'standard' 
                    }
            },
            'loggers': 
            {
                 'django': 
                    {
                        'handlers': ['logfile'],
                        'level': 'CRITICAL',
                        'propagate': True,
                    }
            }
 }
 
 
In case you need your filename to be different, edit the part highlighted in ‘yellow’ color.
Make sure to add the below code or modify the existing ‘DEBUG’ parameter to true, otherwise logging won’t work.

DEBUG = True
 
**STEP-2**
 
Add the following code inside the files serving as ‘View’ of your Django application.
 
- import logging
- logger = logging.getLogger('django')
 
Add below code inside the functions which we are interested to troubleshoot.
Make sure to convert Json response to string before modifying it with ‘logger.critical’
- logger.critical("More Hello")
 
Re-deploy the application with the above changes and reproduce the issue.
Later, we can download the file using FTP from the location mentioned in the filename settings.
 
**ADDITIONAL INFORMATION**
 
In case you want the content from logger statements to be written to default docker logs which we pulled earlier from api/dump endpoint, instantiate the ‘logger’ in the ‘View’ file with the following statement and remove or comment out logger = logging.getLogger('django') code.
logger=logging.getLogger(__name__)
 
 
**FUTURE ADVISE**
Since we are adding the DEBUG=True only for troubleshooting purposes, I would advise to turn it off later by modifying it to DEBUG = os.environ[‘DEBUG’] and set the following in your App Settings under the configuration blade in the portal. 
 
key: DEBUG 
value: 0
 
Source- https://docs.microsoft.com/en-us/azure/app-service/configure-language-python#production-settings-for-django-apps![image](https://user-images.githubusercontent.com/75340668/117064556-556aea80-acf4-11eb-8105-cfbabfe5497b.png)
