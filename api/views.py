from django.shortcuts import render
from django.http import JsonResponse

from .models import Task
# from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.auth import AuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User

@api_view(['GET'])

def apiOverview(request):
    api_urls = {
        'overview': 'api/v1/',
        'create': 'api/v1/create/',
        'update': 'api/v1/update/<int:id>/',
        'delete': 'api/v1/delete/<int:id>/',
        'list': 'api/v1/list/',
        'detail view': 'api/v1/detail/<int:id>/',
        'register': 'api/v1/register/',
    }
    return Response(api_urls)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def taskList(request):
    tasks = Task.objects.all()
    serializers = TaskSerializer(tasks, many=True)
    return Response(serializers.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializers = TaskSerializer(tasks, many=False)
    return Response(serializers.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def taskCreate(request):
    serializers = TaskSerializer(data=request.data)

    if serializers.is_valid():
        serializers.save()

    return Response(serializers.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def taskUpdate(request, pk):
    tasks = Task.objects.get(id=pk)
    serializers = TaskSerializer(instance=tasks, data=request.data)

    if serializers.is_valid():
        serializers.save()

    return Response(serializers.data)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def taskDelete(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return Response('Items successfully deleted')

@api_view(['POST'])
def register_api(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        token_obj, _ = Token.objects.get_or_create(user=user)

    return Response({'data':serializer.data , 'token':str(token_obj)})
