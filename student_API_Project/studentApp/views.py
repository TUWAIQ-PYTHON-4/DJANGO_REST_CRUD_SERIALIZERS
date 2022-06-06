from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer


@api_view(['POST'])
def add_student(request: Request):
    new_student = StudentSerializer(data=request.data)
    if new_student.is_valid():
        new_student.save()
        dataResponse = {
            "msg": "added new student successfully.",
            "student": new_student.data
        }
        return Response(dataResponse)
    else:
        print(new_student.errors)
        dataResponse = {
            "msg": "couldn't add the student."
        }
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_students(request: Request):
    students = Student.objects.all()

    dataResponse = {
        "msg": "list of all students.",
        "students": StudentSerializer(instance=students, many=True).data
    }
    return Response(dataResponse)


@api_view(['DELETE'])
def delete_student(request: Request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    data = {
        "msg": "student is deleted."
    }
    return Response(data)


@api_view(['PUT'])
def update_student(request: Request, student_id):
    student = Student.objects.get(id=student_id)
    updated_info = StudentSerializer(instance=student, data=request.data)
    if updated_info.is_valid():
        updated_info.save()
        dataResponse = {
            "msg": "student information is updated."
        }

        return Response(dataResponse)
    else:
        print(updated_info.errors)
        dataResponse = {
            "msg": "unable to update."
        }
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def search(request: Request, f_name):
    student = Student.objects.filter(first_name=f_name)

    if student.exists():
        dataResponse = {
            "student": StudentSerializer(instance=student, many=True).data
        }
        return Response(dataResponse)
    else:
        dataResponse = {
            "msg": "There is no student with the given first name in our records."
        }
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def top3(request: Request):
    students_gpa_ordered = Student.objects.all().order_by('-gpa')
    top_three = students_gpa_ordered[0:3]
    dataResponse = {
        "top 3 students": StudentSerializer(instance=top_three, many=True).data
    }
    return Response(dataResponse)
