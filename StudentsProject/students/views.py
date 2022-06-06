from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

# Create your views here.


@api_view(['POST'])
def create_student(request : Request):

    new_student = StudentSerializer(data=request.data)
    if new_student.is_valid():
        new_student.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "student" : new_student.data
        }
        return Response(dataResponse)
    else:
        print(new_student.errors)
        return Response( {"msg" : "couldn't create a student"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_students(request : Request):
    students = Student.objects.all()
    students_list = StudentSerializer(instance=students, many=True).data
    dataResponse = {
        "msg": "List of All Students",
        "students": students_list
    }
    return Response(dataResponse)


@api_view(['PUT'])
def update_student(request: Request,stu_id):
    student = Student.objects.get(id=stu_id)
    updated_student = StudentSerializer(instance=student, data=request.data)
    if updated_student.is_valid():
        updated_student.save()
        dataResponse = {
            "msg": "Updated Student Successfully",
        }
        return Response(dataResponse)
    else:
        print(updated_student.errors)
        return Response({"msg": "couldn't update the student"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_student(request: Request, stu_id):
    student = Student.objects.get(id=stu_id)
    student.delete()
    return Response({"msg" : "Deleted Student Successfully"})

@api_view(['GET'])
def list_top_students(request: Request):
    students_gpa = Student.objects.filter(GPA__gte=4)
    top_students = StudentSerializer(instance=students_gpa, many=True).data
    dataResponse = {
        "msg": "List of Top Students",
        "students": top_students
    }

    return Response(dataResponse, status=status.HTTP_200_OK)

@api_view(['GET'])
def search_student (request: Request, name):
   student_search= Student.objects.filter(firstname__startswith=name.lower())

   student_info = StudentSerializer(instance=student_search,  many=True).data
   if student_info:
       dataResponse = {
           "student": student_info
       }
       return Response(dataResponse)
   else:
       print(student_info.errors)
       return Response({"msg": "couldn't find the student"}, status=status.HTTP_400_BAD_REQUEST)




