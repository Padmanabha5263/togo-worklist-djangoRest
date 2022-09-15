from django.shortcuts import render
import  requests
# Create your views here.

def home(request):
    jsondata = requests.get("http://127.0.0.1:8000/webapi/works/").json()
    return render(request,'html/index.html', context={"data":jsondata})