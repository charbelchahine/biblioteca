import json
from .gateways import get_vtk_log, edit_vtk_log
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

@csrf_exempt
def vtk_logger(request):
    if request.method == 'POST':
        post_req = json.loads(request.body)
        print(request.body)
        print(post_req)
        if 'list' in post_req:
            votes = get_vtk_log()
            print(type(votes))
            votes_json = json.dumps(votes)
            
            return JsonResponse(votes_json, safe=False)
        elif 'vote' in post_req:
            try:
                print(post_req['vote']['name'])
                edit_vtk_log(post_req['vote']['name'])
            except:
                return HttpResponse(404)
            votes = get_vtk_log()
            print(type(votes))
            votes_json = json.dumps(votes)
            return JsonResponse(votes_json, safe=False)
        else:
            return HttpResponse(200)