from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import  requests
import json

from .config import getEmpApi, postWorkApi, putWorkApi
# Create your views here.


@csrf_protect
def home(request):
    if(request.method=='POST'):
        urllink=postWorkApi
        if(request.POST['taskid']!='null'):
            urllink=putWorkApi+str(request.POST['taskid'])
        jsonData={
            "name":request.POST['name'],
            "description":request.POST['description'],
            "enddate":request.POST['enddate'],
            "isWorkDone" : request.POST['isWorkDone'],
            "empId":request.POST['empId']
        }
        resData= requests.post(url=urllink, data=jsonData)
        return JsonResponse(json.loads(resData.text))
    
    jsondata = requests.get(url=getEmpApi).json()
    return render(request,'html/index.html', {"data":jsondata})

def deleteTask(request):
    #to delete worklist
    if(request.method=='POST'):
        resData= requests.delete(url=putWorkApi+str(request.POST['taskid'])) 
        return JsonResponse(json.loads(resData.text))