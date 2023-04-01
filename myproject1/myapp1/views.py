from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.generics import get_object_or_404 

from .models import mymodel
from .serializer import myappSerializer

@api_view (['GET']) #get방식
def ReadAPI(request):
    board = mymodel.objects.all() #모델로부터 데이터 가져오기
    serializer = myappSerializer(board, many=True) # 시리얼라이저에 데이터 넣기  # many=True 왜 하는거임 ??? 
    return Response(serializer.data, status=status.HTTP_200_OK)
# Create your views here.

@api_view(['POST']) #POST방식
def WriteAPI(request):
    serializer = myappSerializer(data=request.data)
    #요청으로 들어온 데이터를 시리얼라이저에 넣기

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    #module 'rest_framework.status' has no attribute 'HTTP_404_BAD_REQUEST'