from django.shortcuts import render
from employee_app.models import Emp
from employee_app.serializer import EmpSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

class EmpDetail(APIView):

  def get(self, request,pk=None):
    if pk is not None:
      q = Emp.objects.get(pk=pk)
      serializer = EmpSerializer(q)
      return Response(serializer.data)
    else:
      q = Emp.objects.all()
      serializer = EmpSerializer(q,many=True)
      return Response(serializer.data)
    
  def post(self,request):
    serializer = EmpSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  def put(self, request, pk, *args, **kwargs):
    q = Emp.objects.get(pk=pk)
    serializer = EmpSerializer(q, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self,request,pk):
    q = Emp.objects.get(pk=pk)
    q.delete()
    return Response("deleted !")

 