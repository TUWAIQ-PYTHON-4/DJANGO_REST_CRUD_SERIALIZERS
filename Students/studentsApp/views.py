from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Students
from .serializers import StudentsSerializer
from rest_framework import status
from collections import Counter
from heapq import nlargest


# Create your views here.

@api_view(['GET'])
def display_students(request: Request):
    students = Students.objects.all()
    dataResponse = {
        "msg": "List of All Students",
        "students": StudentsSerializer(instance=students, many=True).data
    }
    return Response(dataResponse)


@api_view(['POST'])
def add_students(request: Request):
    students = StudentsSerializer(data=request.data)
    if students.is_valid():
        students.save()
        dataResponse = {
            "msg": "Created Successfully",
            "students": students.data
        }
        return Response(dataResponse)
    else:
        print(students.errors)
        dataResponse = {"msg": "couldn't create a student"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_student_info(request: Request, id):
    student = Students.objects.get(id=id)
    updated_student = StudentsSerializer(instance=student, data=request.data)
    if updated_student.is_valid():
        updated_student.save()
        responseData = {
            "msg": "updated successefully"
        }
        return Response(responseData)
    else:
        print(updated_student.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_student(request: Request, id):
    student = Students.objects.get(id=id)
    student.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(["GET"])
def top_3_studens(request: Request):
    students = Students.objects.order_by("-GPA").values("first_name")
    keys = ['student1', 'student2', 'student3']
    values = []
    top_3_students = {}
    for i in range(3):
        values.append(students[i])

    for i in range(len(keys)):
        top_3_students[keys[i]] = values[i]

    return Response(top_3_students)


@api_view(["GET"])
def Search_by_name(request: Request, name):
    student = Students.objects.filter(first_name=name)
    if student.exists():
        return Response({"msg": "Found it"})
    else:
        return Response({"msg": "Not found !!"})
