from django.shortcuts import render
from django.http import JsonResponse
import  requests
import json
# Create your views here.

def home(request):
    if(request.method=='POST'):
        jsonData={
            "name":request.POST['name'],
            "description":request.POST['description'],
            "enddate":request.POST['enddate'],
            "email":request.POST['email'],
            "isWorkDone" : False,
        }
        resData= requests.post(url='http://127.0.0.1:8000/webapi/works/', data=jsonData)
        return JsonResponse(json.loads(resData.text)) 
    jsondata = requests.get(url="http://127.0.0.1:8000/webapi/works/").json()
    return render(request,'html/index.html', context={"data":jsondata})