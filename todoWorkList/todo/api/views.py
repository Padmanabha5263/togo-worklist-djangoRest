from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from todo.models import Worklist
from .serializers import WorklistSerializer



# Create your views here.
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
            return Response(serializer.data)
        return Response(serializer.errors)
        

@api_view(['GET', 'PUT', 'DELETE'])
def todoWork(request, pk):
    try:
        work = Worklist.objects.get(pk=pk)
    except Worklist.DoesNotExist:
        return Response({"Message":"worklist not exist"})

    if(request.method=='GET'):
        serializer = WorklistSerializer(work, many=False)
        return Response(serializer.data)

    if(request.method=='PUT'):
        serializer = WorklistSerializer(work, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    if(request.method=='DELETE'):
        work.delete()
        return Response({"message":"work deleted successfully"}, status=status.HTTP_200_OK)  
            

