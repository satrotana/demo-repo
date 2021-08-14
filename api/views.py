from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Employee
from .serializers import EmployeeSerializer, UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# api no interface
@csrf_exempt
def employeeListView(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        serializer = EmployeeSerializer(data = jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)

@csrf_exempt
def employeeDetailView(request, pk):
    try:
        employee = Employee.objects.get(id=pk)
    except Employee.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data, safe=False)
    elif request.method =='DELETE':
        employee.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)
    elif request.method =='PUT':
        jsonData = JSONParser().parse(request)
        serializer = EmployeeSerializer(employee, data = jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)

@csrf_exempt
def UserListView(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)

# with interface
@api_view(['GET','POST'])
def employeeListInterface(request):
    if request.method == 'GET':
            employee = Employee.objects.all()
            serializer = EmployeeSerializer(employee, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','DELETE','PUT'])
def employeeDetailInterface(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method =='DELETE':
        employee.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    elif request.method =='PUT':
        serializer = EmployeeSerializer(employee, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)