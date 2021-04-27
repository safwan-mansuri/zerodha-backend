from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .adapter.redis_adapter import RedisAdapter
from django.views.decorators.csrf import csrf_exempt
import numpy, json, redis, os
from urllib.parse import urlparse
from .constants import REDIS_URL, LIST_NAME
import logging

logging.basicConfig(level=logging.DEBUG)

url = urlparse(REDIS_URL)
r = redis.Redis(
  host=url.hostname, 
  port=url.port,
  decode_responses=True,
  password=url.password
)

ra = RedisAdapter(r, LIST_NAME)

def stockDetails(request) :
  try :
    logging.info('stockDetails entry point ..........')
    data = ra.showAll()
    date = r.get('date')
    response = {
      "statusCode": 200,
      "data": data,
      "date": date
    }
    return JsonResponse(json.dumps(response), safe=False)
  except Exception as e:
    logging.error('Something bad happened', str(e))
    response = {
      "statusCode": 500,
      "error_message": str(e)
    }
    return JsonResponse(json.dumps(response), safe=False)

@csrf_exempt
def todayData(request) :
  logging.info('todayData entry point ..........')
  try :
    if request.method == 'POST' :
      ra.removeAll()
      r.delete('date')
      data = json.loads(request.POST.get('equity'))
      date = request.POST.get('date')
      for d in numpy.array(data['data']) :
        ra.append(d)
      r.set('date', date)
    response = {
      "statusCode": 200,
      "success": True
    }
    return JsonResponse(json.dumps(response), safe=False)
  except Exception as e:
    logging.error('Something bad happened', str(e))
    response = {
      "statusCode": 500,
      "error_message": str(e)
    }    
    return JsonResponse(json.dumps(response), safe=False)
