from django.shortcuts import render
from os import stat
from urllib import response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import StudentsInfo
from .serializers import StudentsSerializer



@api_view(['GET'])
def list_student(request : Request):
    info_student = StudentsInfo.objects.all()

    dataResponse = {
        "msg" : "List of All Students",
        "students" : StudentsSerializer(instance=info_student, many=True).data
    }

    return Response(dataResponse)



@api_view(['POST'])
def add_students(request : Request):

    new_student = StudentsSerializer(data=request.data)
    if new_student.is_valid():
        new_student.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "new_student" : new_student.data
        }
        return Response(dataResponse)
    else:
        print(new_student.errors)
        dataResponse = {"msg" : "couldn't create a Student Info"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_studet(request : Request, student_id):
    student = StudentsInfo.objects.get(id=student_id)

    update_studet = StudentsSerializer(instance=student, data=request.data)
    if update_studet.is_valid():
        update_studet.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(update_studet.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
def delete_student(request: Request, student_id):
    student = StudentsInfo.objects.get(id=student_id)
    student.delete()
    return Response({"msg" : "Deleted Successfully"})


@api_view(["GET"])
def search_student(request: Request, name):
    student = StudentsInfo.objects.filter(first_name=name)
    if student.exists():
        return Response({"msg": "Found it"})
    else:
        return Response({"msg": "Not found!!"})

