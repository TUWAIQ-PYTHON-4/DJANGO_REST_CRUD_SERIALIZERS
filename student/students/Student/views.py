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
    lst_student = Students.GPA
    highest_grade = 0  # "max" is a terrible name for a variable
    for student, grade in Students:
        if grade > highest_grade:
            lst_student = highest_grade
            best_student = student
    return highest_grade, lst_student


bstudent, bgrade = best_student_grade()

print(f"The best student is: {bstudent} with a {bgrade}")
