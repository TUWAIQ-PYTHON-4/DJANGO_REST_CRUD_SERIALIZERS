from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer


# Create your views here.

@api_view(['POST'])
def add_student(request: Request):
    student = StudentSerializer(data=request.data)
    if student.is_valid():
        student.save()
        dataResponse = {
            "msg": " Student Added Successfully",
            "student": student.data
        }
        return Response(dataResponse)
    else:
        print(student.errors)
        dataResponse = {"msg": "couldn't add student"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_students(request: Request):
    student = Student.objects.all()
    dataResponse = {
        'msg': 'List of All Students',
        'Students': StudentSerializer(instance=student, many=True).data
    }
    return Response(dataResponse)


@api_view(['PUT'])
def update_student(request: Request, student_id):
    student = Student.objects.get(id=student_id)
    student_updated = StudentSerializer(instance=student, data=request.data)
    if student_updated.is_valid():
        student_updated.save()
        responseData = {
            'msg': 'Student Updated Successfully'
        }
        return Response(responseData)
    else:
        print(student_updated.errors)
        return Response({'msg': 'bad request, could not update'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_student(request: Request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return Response({'msg': 'Student Deleted Successfully'})


@api_view(['GET'])
def top_students(request: Request):
    student = Student.objects.all().order_by('-GPA')[:3]
    dataResponse = {
        'msg': 'List of Top Students',
        'Students': StudentSerializer(instance=student, many=True).data
    }
    return Response(dataResponse)


@api_view(['GET'])
def search(request: Request):
    if request.method == 'GET':
        students = Student.objects.all()
        first_name = request.GET.get('first_name', None)
        if first_name is not None:
            students = students.filter(first_name__icontains=first_name)

        dataResponse = {
            'mas': 'Search By Name',
            'Students': StudentSerializer(students, many=True).data
        }
        return Response(dataResponse)
