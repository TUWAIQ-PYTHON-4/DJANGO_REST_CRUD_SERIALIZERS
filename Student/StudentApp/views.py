import heapq
from os import stat
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import StudentSerializer


# Create your views here.


@api_view(['POST'])
def add_student(request: Request):
    new_student = StudentSerializer(data=request.data)
    if new_student.is_valid():
        new_student.save()
        dataResponse = {
            "msg": "Created Student Successfully",
            "student": new_student.data
        }
        return Response(dataResponse)
    else:
        print(new_student.errors)
        dataResponse = {"msg": "couldn't create a Student"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_student(request: Request):
    student = Student.objects.all()

    dataResponse = {
        "msg": "List of All Students",
        "student": StudentSerializer(instance=student, many=True).data
    }
    return Response(dataResponse)


@api_view(['PUT'])
def update_student(request: Request, student_id):
    student = Student.objects.get(id=student_id)

    updated_std = StudentSerializer(instance=student, data=request.data)
    if updated_std.is_valid():
        updated_std.save()
        responseData = {
            "msg": "updated student successfully"
        }

        return Response(responseData)
    else:
        print(updated_std.errors)
        return Response({"msg": "cannot update student !! "}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_student(request: Request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['GET'])
def list_top3(request: Request):
    top = Student.objects.all().order_by('GPA')[0:3]

    dataResponse = {
        "msg": "List of Top 3 Students",
        "student": StudentSerializer(instance=top, many=True).data
    }
    return Response(dataResponse)


@api_view(['GET'])
def search_std(request: Request, first_name1):
    student = Student.objects.filter(first_name=first_name1)
    dataResponse = {
        "msg": "Search :",
        "student": StudentSerializer(instance=student, many=True).data
    }
    return Response(dataResponse)
