import imp
from os import stat
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer





@api_view(['POST'])
def add_student(request : Request):

    new_student = StudentSerializer(data=request.data)
    if new_student.is_valid():
        new_student.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "student" : new_student.data}
        return Response(dataResponse)
    else:
        print(new_student.errors)
        dataResponse = {"msg" : "couldn't create a city"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_students(request : Request):
    students = Student.objects.all()

    dataResponse = {
        "msg" : "List of All Students",
        "students" : StudentSerializer(instance=students, many=True).data
        }

    return Response(dataResponse)

@api_view(['PUT'])
def update_student(request : Request, student_id):
    student = Student.objects.get(id=student_id)

    updated_student = StudentSerializer(instance=student, data=request.data)
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
    student = Student.objects.get(id=student_id)
    student.delete()
    return Response({"msg" : "Deleted Successfully"})


@api_view(['GET'])
def list_top3(request: Request):
    top = Student.objects.all().order_by('-GPA')[0:3]

    dataResponse = {
        "msg": "List of Top 3 Students",
        "student": StudentSerializer(instance=top, many=True).data
    }
    return Response(dataResponse)


@api_view(['GET'])
def search_std(request: Request, name):
    student = Student.objects.filter(first_name=name)
    dataResponse = {
        "msg": "Search :",
        "student": StudentSerializer(instance=student, many=True).data
    }
    return Response(dataResponse)


