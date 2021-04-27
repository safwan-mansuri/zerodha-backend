from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .adapter.redis_adapter import RedisAdapter
from django.views.decorators.csrf import csrf_exempt
import numpy, json, redis, os

r = redis.Redis(host='redis', port=6379, decode_responses=True)

ra = RedisAdapter(r, 'stocks')

def stockDetails(request) :
  data = ra.showAll()
  date = r.get('date')
  response = {
    "statusCode": 200,
    "data": data,
    "date": date
  }

  return JsonResponse(json.dumps(response), safe=False)

@csrf_exempt
def todayData(request) :
  if request.method == 'POST' :
    ra.removeAll()
    r.delete('date')
    data = json.loads(request.POST.get('equity'))
    date = request.POST.get('date')
    print(date)
    for d in numpy.array(data['data']) :
      ra.append(d)
    r.set('date', date)
    print('done traveresiong')
  return HttpResponse('hello')
