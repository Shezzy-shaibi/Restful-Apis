from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
 
from .models import Student
from .serializers import StudentSrl
 
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def query_to_json(request):
    if request.method == "GET":
        print(">>>>> Get")
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythDict = JSONParser().parse(stream)
        id = pythDict.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serl = StudentSrl(stu)
            # jsn = JSONRenderer().render(serl.data)
            # return HttpResponse(jsn, content_type="application/json")
            return JsonResponse(serl.data)
        studs = Student.objects.all()
        serls = StudentSrl(studs,many=True)
        return JsonResponse(serls.data, safe=False)

    if request.method == "POST":
        jsn_data = request.body
        stream = io.BytesIO(jsn_data)
        dicts = JSONParser().parse(stream)
        ser = StudentSrl(data=dicts)
        if ser.is_valid():
            ser.save()
            resp = {'result':'sucess','msg':'Data is created successfully'}
            return JsonResponse(resp)