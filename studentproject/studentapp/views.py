from os import stat
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import student
from .serializers import studentSerializer
from rest_framework.filters import SearchFilter
#from django_filters.rest_framework import DjangoFilterBackend

@api_view(['POST'])
def add_student(request : Request):

    new_student = studentSerializer(data=request.data)
    if new_student.is_valid():
        new_student.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "student" : new_student.data
        }
        return Response(dataResponse)
    else:
        print(new_student.errors)
        dataResponse = {"msg" : "couldn't create a student"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_student(request : Request):
    students = student.objects.all()

    dataResponse = {
        "msg" : "List of All student",
        "student" : studentSerializer(instance=students, many=True).data
    }

    return Response(dataResponse)

@api_view(['PUT'])
def update_student(request : Request, student_id):
    student_update = student.objects.get(id=student_id)

    updated_student = studentSerializer(instance=student_update, data=request.data)
    if updated_student.is_valid():
        updated_student.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_student.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request: Request, student_id):
    student_dalete = student.objects.get(id=student_id)
    student_dalete.delete()
    return Response({"msg" : "Deleted Successfully"})


@api_view(['GET'])
def search(request: Request , first_name):
    student_search = student.objects.filter(first_name=first_name)
    Student = {
        "msg" : "done",
        "student" : studentSerializer(instance=student_search, many=True).data
    }
    return Response(Student)
    

@api_view(['GET'])
def orderingviws(request: Request):
    student_order = student.objects.all().order_by('GPA')
    Student = {
        "msg": "done",
        "student": studentSerializer(instance=student_order, many=True).data
    }
    return Response(Student)

