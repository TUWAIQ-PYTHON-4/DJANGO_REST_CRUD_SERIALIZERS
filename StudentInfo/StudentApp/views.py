from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer


# Create your views here.
@api_view(['POST'])
def new_student(request: Request):
    new_student = StudentSerializer(data=request.data)
    if new_student.is_valid():
        new_student.save()
        dataResponse = {
            "msg": "Created Successfully",
            "new_student": new_student.data
        }
        return Response(dataResponse)
    else:
        print(new_student.errors)
        dataResponse = {"msg": "couldn't create a student"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_student(request: Request):
    students = Student.objects.all()

    dataResponse = {
        "msg": "List of All students",
        "student": StudentSerializer(instance=students, many=True).data
    }
    return Response(dataResponse)


@api_view(['PUT'])
def update_student(request: Request, student_id):
    student_info = Student.objects.get(id=student_id)

    updated_student = StudentSerializer(instance=student_info, data=request.data)
    if updated_student.is_valid():
        updated_student.save()
        responseData = {
            "msg": "updated successefully"
        }

        return Response(responseData)
    else:
        print(update_student.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_student(request: Request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return Response({"msg": "Deleted Successfully"})


# Search Function
@api_view(['GET'])
def search(request: Request, first_name):
    studen_filter = Student.objects.filter(first_name=first_name)
    dataResponse = {
        "msg": "you search student :",
        "studen_filter": StudentSerializer(instance=studen_filter, many=True).data
    }
    return Response(dataResponse)


@api_view(['GET'])
def List_top_GPA(request: Request):
            students_order = Student.objects.order_by('-GPA')
            student=StudentSerializer(instance=students_order, many=True).data
            dataResponse = {
                "msg": "List_top_GPA :",
                "studen_top_GPA": student[:3]
            }
            return Response(dataResponse)
