from django.shortcuts import render
from os import stat
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


from .models import students
from .serializers import syudentsSerializer

# Create your views here.

@api_view(['POST'])
def add_student(request : Request):

    new_student = syudentsSerializer(data=request.data)
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
    stuednts = students.objects.all()

    dataResponse = {
        "msg" : "List of All students",
        "students" : syudentsSerializer(instance=stuednts, many=True).data
    }

    return Response(dataResponse)







@api_view(['PUT'])
def update_student(request : Request, students_id):
    city = students.objects.get(id=students_id)

    updated_student = syudentsSerializer(instance=city, data=request.data)
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
def delete_student(request: Request, students_id):
    student = students.objects.get(id=students_id)
    student.delete()
    return Response({"msg" : "Deleted Successfully"})

@api_view(['GET'])
def search_student(request : Request ,first_name):
    stuednts = students.objects.filter(f_name=first_name)

    dataResponse = {
        "msg" : "the name :",
        "students" : syudentsSerializer(instance=stuednts, many=True).data
    }

    return Response(dataResponse)

@api_view(['GET'])
def top3_GPA(request : Request ):
    stuednts = students.objects.filter().order_by('-GPA')[0:3]


    dataResponse = {
        "msg" : "top 3 GPA :",
        "students" : syudentsSerializer(instance=stuednts, many=True).data
    }

    return Response(dataResponse)




