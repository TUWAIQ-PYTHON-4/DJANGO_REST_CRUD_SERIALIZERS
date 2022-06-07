from os import stat
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer


@api_view(['POST'])
def add_student(request: Request):
    new_student = StudentSerializer(data=request.data)
    if new_student.is_valid():
        new_student.save()
        dataResponse = {
            "msg": "Created Successfully",
            "student": new_student.data
        }
        return Response(dataResponse)
    else:
        print(new_student.errors)
        dataResponse = {"msg": "couldn't create a new student"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_student(request: Request):
    students = Students.objects.all()

    dataResponse = {
        "msg": "List of Students",
        "Students": StudentSerializer(instance=students, many=True).data
    }

    return Response(dataResponse)


@api_view(['GET'])
def update_student(request: Request, students_id):
    student = Students.objects.get(id=students_id)

    updated_student = StudentSerializer(instance=student, data=request.data)
    if updated_student.is_valid():
        updated_student.save()
        responseData = {
            "msg": "updated successfully"
        }

        return Response(responseData)
    else:
        print(updated_student.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_student(request: Request, students_id):
    student = Students.objects.get(id=students_id)
    student.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['GET'])
def best_student_grade(request: Request):
    lst_student = Students.objects.all().order_by('GPA')[0:3]

    top_students = {

        "student": StudentSerializer(instance=lst_student, many=True).data

    }

    return Response(top_students)


@api_view(['GET'])
def search_students(request: Request, new_name):
    search_s = Students.objects.filter(first_name=new_name)
    search_student = {
        "student": StudentSerializer(instance=search_s, many=True).data
    }
    return Response(search_student)
