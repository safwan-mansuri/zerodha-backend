from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .adapter.redis_adapter import RedisAdapter
from django.views.decorators.csrf import csrf_exempt
import numpy, json, redis, os
from urllib.parse import urlparse

url = urlparse("redis://redistogo:d4323775a9c4ca398d9363c0d304e962@scat.redistogo.com:11835/")
print(url)
print('hostname', url.hostname)
print('port', url.port)
print(url.password)
r = redis.Redis(
  host=url.hostname, 
  port=url.port,
  decode_responses=True,
  password=url.password
)

ra = RedisAdapter(r, 'stocks')

def stockDetails(request) :
  print('hello')
  data = ra.showAll()
  date = r.get('date')
  print(data, date)
  response = {
    "statusCode": 200,
    "data": data,
    "date": date
  }

  return JsonResponse(json.dumps(response), safe=False)

@csrf_exempt
def todayData(request) :
  print('####################################')
  if request.method == 'POST' :
    ra.removeAll()
    r.delete('date')
    data = json.loads(request.POST.get('equity'))
    date = request.POST.get('date')
    print(date)
    for d in numpy.array(data['data']) :
      ra.append(d)
    r.set('date', date)
    print('done traversing')
  return HttpResponse('hello')
