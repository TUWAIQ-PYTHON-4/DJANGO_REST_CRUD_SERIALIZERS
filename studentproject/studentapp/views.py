from os import stat
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status , DjangoFilterBackend
from .models import student
from .serializers import studentSerializer
from rest_framework.filters import SearchFilter

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
def update_student(request : Request, city_id):
    student_update = student.objects.get(id=city_id)

    updated_city = studentSerializer(instance=student_update, data=request.data)
    if updated_city.is_valid():
        updated_city.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_city.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request: Request, student_id):
    student_dalete = student_id.objects.get(id=student_id)
    student_dalete.delete()
    return Response({"msg" : "Deleted Successfully"})


@api_view(['GET'])
def search(request: Request):
    student_search = student.objects.all()
    serilaiz_student= studentSerializer()
    filter_backends = (DjangoFilterBackend , SearchFilter)
    fitter_fields = ('first_name')

@api_view(['GET'])
def orderingviws(request: Request):
    student_order = student.objects.all()
    after_order = sorted(student_order , key=student_order['GPA'] )
