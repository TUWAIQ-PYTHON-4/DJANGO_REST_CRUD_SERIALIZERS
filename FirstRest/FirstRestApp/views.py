
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from datetime import date as my_date
from random import randint

from .models import *
from .serializers import *

@api_view(['GET'])
def date(request : Request):
    data = {
        "date" : f"Today is {my_date.today()}"
    }

    return Response(data)

@api_view(["POST"])
def random(request: Request):

    min =  request.data.get("min", None)
    max = request.data.get('max', None)

    if min < 0 or min > max:
        data = {
         "msg": "Not Allowed. Please provide a min that is bigger than 0 and a max bigger than the min"}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    else:
        random = randint(min, max)
        data = {
         "random": random }
        return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_student(request : Request):

    new_student = StudentSerializer(data=request.data)
    if new_student.is_valid():
        new_student.save()
        dataResponse = {
            "msg" : "Student added Successfully",
            "student" : new_student.data
        }
        return Response(dataResponse)
    else:
        print(new_student.errors)
        dataResponse = {"msg" : "couldn't add a student"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_students(request : Request):
    students = Student.objects.all()

    dataResponse = {
        "msg" : "List of All students",
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
            "msg" : "Student info updated successefully!"
        }

        return Response(responseData)
    else:
        print(updated_student.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request: Request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return Response({"msg" : "Student deleted Successfully"})

@api_view(['GET'])
def list_top_students(request : Request):
    top_students = Student.objects.all().order_by('-GPA')[:3]

    dataResponse = {
        "msg" : "List of top students",
        "students" : StudentSerializer(instance=top_students, many=True).data
    }

    return Response(dataResponse)

@api_view(['GET'])
def search_for_student(request : Request, student_first_name ,student_last_name):
    student = Student.objects.get(first_name=student_first_name,last_name=student_last_name)

    dataResponse = {
        "msg" : "Search resualt",
        "student" : StudentSerializer(instance=student).data
    }

    return Response(dataResponse)




