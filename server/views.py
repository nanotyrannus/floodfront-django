from json import loads
from django.shortcuts import render
from django.db.models import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import User, Marker
from .forms import UploadedFileForm

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
        email = loads(request.body.decode(encoding='utf-8'))['email']
        if not User.objects.filter(email=email).exists():
            u = User(email=email)
            u.save()
            res = JsonResponse({
                'email' : email,
                'message' : 'New email added.'
            })
        else:
            res = JsonResponse({
                'email' : email
            })
        return res
    else:
        return HttpResponseNotAllowed(['POST','OPTIONS'])

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
    else:
        return HttpResponseNotAllowed(['POST','OPTIONS'])

@csrf_exempt
def delete_marker(request, **kwargs):
    if request.method == 'POST':
        id = kwargs['marker_id']
        print('Delete Marker with ID {}'.format(id))
        if Marker.objects.filter(id=id).delete()[0] > 0:
            return JsonResponse({
                'status' : 'success',
                'marker_id' : id,
                'action' : 'delete'
            })
        else:
            return JsonResponse({
                'status' : 'failure',
                'marker_id' : id,
                'action' : 'delete',
                'message' : 'No marker found with id {}.'.format(id)
            })
    else:
        return HttpResponseNotAllowed(['POST'])

@csrf_exempt
def add_description(request, **kwargs):
    id = kwargs['marker_id']
    data = loads(request.body)
    desc = data['description']
    if Marker.objects.filter(id=id).update(description=desc) > 0:
        return JsonResponse({
            'status' : 'success',
            'marker_id' : id,
            'action' : 'add-description'
        })
    else:
        return JsonResponse({
            'status' : 'failure',
            'message' : 'Marker not found',
            'action' : 'add-description'
        })

@csrf_exempt
def upload_image(request, **kwargs):
    print("Upload image.")
    if request.method == 'POST':
        form = UploadedFileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print("Valid form")
            data = form.cleaned_data
            print(data)
            image = request.FILES.get('image')
            if 'jpeg' in image.content_type or 'jpg' in image.content_type:
                name = "{}.jpg".format(data['marker_id'])
            elif 'png' in image.content_type:
                name = "{}.png".format(data['marker_id'])
            upload_handler(image, name)
        else:
            print("Invalid")
            print(form.errors)
    return JsonResponse({
        'action' : 'upload-image'
    })

import os

def upload_handler(f, file_name):
    dest = os.path.join('uploads', file_name)
    with open(dest, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)