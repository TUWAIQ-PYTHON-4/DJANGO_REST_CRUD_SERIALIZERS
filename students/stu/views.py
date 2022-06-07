from ast import Return
import imp
from turtle import st
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import students
from .serializers import StuSerilizer

# Create your views here.

@api_view(['POST'])
def add_stu(request:Request):
    new_stu = StuSerilizer(data=request.data)
    if new_stu.is_valid():
        dataResponse = {
            'msg' : 'Added Successfully',
            'student' : new_stu.data
        }
        return Response(dataResponse)
    else:
        dataResponse = {'msg' : 'Couldn\'t add a student'}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_stu(request : Request):
    stu = students.objects.all()

    dataResponse = {
        "msg" : "List of All students",
        "students" : StuSerilizer(instance=stu, many=True).data
    }

    return Response(dataResponse)


@api_view(['PUT'])
def update_stu(request : Request, student_id):
    stu = students.objects.get(id=student_id)

    updated_stu = StuSerilizer(instance=stu, data=request.data)
    if updated_stu.is_valid():
        updated_stu.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_stu(request: Request, student_id):
    student = students.objects.get(id=student_id)
    student.delete()
    return Response({"msg" : "Deleted Successfully"})
