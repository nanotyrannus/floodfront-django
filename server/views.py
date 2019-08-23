from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from datetime import datetime
from .models import User, Marker
from django.views.decorators.csrf import csrf_exempt
from json import loads
from django.db.models import ObjectDoesNotExist

@csrf_exempt
def ping(request):
    return JsonResponse({
        'time':"{:%s}".format(datetime.now()),
        'message':'Response from floodfront server.'
    })

# Lazy account creation and login
@csrf_exempt
def login(request):
    if request.method == 'POST' or request.method == 'OPTIONS':
        res = JsonResponse({
            'email' : 'test@email.com'
        })
        return res
    else:
        return JsonResponse({
            'error' : 'You must POST to this endpoint.'
        })

@csrf_exempt
def get_markers(request):
    if request.method == 'POST' or request.method == 'OPTIONS':
        res = {}
        if len(request.body) != 0:
            email = loads(request.body.decode(encoding='utf-8'))['email']
            res = {
                'markers' : list(Marker.objects.filter(email=email).values())
            }
        return JsonResponse(res)
    else:
        return HttpResponseNotAllowed(['POST', 'OPTIONS'])
    
@csrf_exempt
def create_marker(request):
    if request.method == 'POST' or request.method == 'OPTIONS':
        body = {
            'action' : 'create'
        }
        if len(request.body) != 0:
            marker_data = loads(request.body.decode(encoding='utf-8'))
            marker = Marker(
                marker_type=marker_data['type'],
                lat=marker_data['lat'],
                lon=marker_data['lon'],
                heading=marker_data['heading'],
                accuracy=marker_data['accuracy'],
                email=marker_data['email'],
            )
            marker.save()
            print(marker.id)
            body['id'] = marker.id
        return JsonResponse(body)
    else:
        return HttpResponseNotAllowed(['POST','OPTIONS'])

@csrf_exempt
def update_marker(request, **kwargs):
    if request.method == 'POST' or request.method == 'OPTIONS':
        if len(request.body) != 0:
            id = kwargs['marker_id']
            data = loads(request.body)
            print("Marker stuff!: {}".format(loads(request.body)['lon']))
            marker = Marker.objects.get(id=id)
            Marker.objects.filter(id=id).update(lat=data['lat'], lon=data['lon'])

    return JsonResponse({
        'status' : 'success',
        'marker_id' : kwargs['marker_id'],
        'action' : 'update'
    })

@csrf_exempt
def delete_marker(request, **kwargs):
    id = kwargs['marker_id']
    print('Delete Marker with ID {}'.format(id))
    Marker.objects.filter(id=id).delete()
    return JsonResponse({
        'status' : 'success',
        'marker_id' : id,
        'action' : 'delete'
    })