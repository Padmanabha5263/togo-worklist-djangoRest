from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from todo.models import Worklist, Employees, Superiors
from .serializers import WorklistSerializer, EmployeelistSerializer, SupervisorSerializer



# Create your views here.
#http://127.0.0.1:8000/webapi/works/
@api_view(['GET', 'POST'])
def todoWorks(request):
    if(request.method=='GET'):
        work = Worklist.objects.all()
        serializer = WorklistSerializer(work, many=True)
        return Response(serializer.data)
    
    if(request.method=='POST'):
        serializer=WorklistSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)        

#http://127.0.0.1:8000/webapi/works/1
@api_view(['GET', 'POST', 'DELETE'])
def todoWork(request, pk):
    try:
        work = Worklist.objects.get(pk=pk)
    except Worklist.DoesNotExist:
        return Response({"Message":"worklist not exist"})

    if(request.method=='GET'):
        serializer = WorklistSerializer(work, many=False)
        return Response(serializer.data)

    if(request.method=='POST'):
        serializer = WorklistSerializer(work, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    if(request.method=='DELETE'):
        work.delete()
        return Response({"message":"work deleted successfully"}, status=status.HTTP_200_OK)  



#http://127.0.0.1:8000/webapi/employees
@api_view(['GET', 'POST'])
def todoEmployees(request):
    if(request.method=='GET'):
        employees = Employees.objects.all()
        serializer = EmployeelistSerializer(employees, many=True)
        return Response(serializer.data)
    
    if(request.method=='POST'):
        serializer=EmployeelistSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)        

@api_view(['GET', 'PUT', 'DELETE'])
def todoEmployee(request, pk):
    try:
        employee = Employees.objects.get(pk=pk)
    except Employees.DoesNotExist:
        return Response({"Message":"employee not exist"})

    if(request.method=='GET'):
        serializer = EmployeelistSerializer(employee, many=False)
        return Response(serializer.data)

    if(request.method=='PUT'):
        serializer = EmployeelistSerializer(employee, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    if(request.method=='DELETE'):
        employee.delete()
        return Response({"message":"employee deleted successfully"}, status=status.HTTP_200_OK)  


#http://127.0.0.1:8000/webapi/employees
@api_view(['GET', 'POST'])
def todoSupervisors(request):
    if(request.method=='GET'):
        sprvirs = Superiors.objects.all()
        serializer = SupervisorSerializer(sprvirs, many=True)
        return Response(serializer.data)
    
    if(request.method=='POST'):
        serializer=SupervisorSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)        

@api_view(['GET', 'PUT', 'DELETE'])
def todoSupervisor(request, pk):
    try:
        sprvirs = Superiors.objects.get(pk=pk)
    except Superiors.DoesNotExist:
        return Response({"Message":"Supervisors not exist"})

    if(request.method=='GET'):
        serializer = SupervisorSerializer(sprvirs, many=False)
        return Response(serializer.data)

    if(request.method=='PUT'):
        serializer = SupervisorSerializer(sprvirs, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    if(request.method=='DELETE'):
        sprvirs.delete()
        return Response({"message":"Supervisors deleted successfully"}, status=status.HTTP_200_OK)  