import operator
from heapq import nlargest
from urllib.request import Request
from warnings import filters
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer, TopStudentSerializer
from .models import Student


@api_view(['POST'])
def add_student(request: Request):
    new_student = StudentSerializer(data=request.data)
    if new_student.is_valid():
        new_student.save()
        dataResponse = {
            "msg": "Created Student Successfully",
            "student": new_student.data
        }
        return Response(dataResponse)
    else:
        print(new_student.errors)
        dataResponse = {"msg": "couldn't create student"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_student(request: Request):
    students = Student.objects.all()
    dataResponse = {
        "msg": "List all students",
        "Students": StudentSerializer(instance=students, many=True).data

    }

    return Response(dataResponse)


@api_view(['PUT'])
def update_student(request: Request, student_id):
    student = Student.objects.get(id=student_id)

    updated_student = StudentSerializer(instance=student, data=request.data)
    if updated_student.is_valid():
        updated_student.save()
        responseData = {
            "msg": "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_student.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_students(request: Request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['GET'])
def top3_student(request: Request, ARM=None):
    students = Student.objects.filter().order_by('gpa')[0:3]

    dataResponse = {
        "ARM": StudentSerializer(instance=students, many=True).data
    }

    return Response(dataResponse)





@api_view(['GET'])
def search_name(request: Request, name):
    student = Student.objects.filter(first_name=name)
    dataResponse = {
        "msg": "Search by name:",
        "student": StudentSerializer(instance=student, many=True).data
    }

    return Response(dataResponse)




