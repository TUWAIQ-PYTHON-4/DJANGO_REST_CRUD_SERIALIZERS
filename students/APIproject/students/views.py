from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentsSerializer

@api_view(['POST'])
def add_student(request : Request):

    student =StudentsSerializer(data=request.data)
    if student.is_valid():
        student.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "student" : student.data
        }
        return Response(dataResponse)
    else:
        print(student.errors)
        dataResponse = {"msg" : "couldn't create a student"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_Students(request : Request):
    student = Students.objects.all()
    #student = Students.objects.order_by('GPA')[:3]

    dataResponse = {
        "msg" : "List of All Students",
        "Students" : StudentsSerializer(instance=student, many=True).data
    }

    return Response(dataResponse)




@api_view(['PUT'])
def update_Student(request : Request, Student_id):
    Student = Students.objects.get(id=Student_id)

    update_Student = StudentsSerializer(instance=Student, data=request.data)
    if update_Student.is_valid():
        update_Student.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(update_Student.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_Student(request: Request, Student_id):
    Student = Students.objects.get(id=Student_id)
    Student.delete()
    return Response({"msg" : "Deleted Successfully"})


def search_Student(request):

    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Students.objects.filter(name__contains=query_name)
            dataResponse = {
                "msg": "Created Successfully",
                "student": query_name.data
            }
            return Response(dataResponse,results)
            #return render(request, 'product-search.html', {"results":results})

        dataResponse = {"msg": "couldn't create a student"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def search_name(request: Request, name):
    student = Students.objects.filter(first_name=name)
    dataResponse = {
        "msg": "Search by name:",
        "student": StudentsSerializer(instance=student, many=True).data
    }

    return Response(dataResponse)



@api_view(['GET'])
def top_student(request: Request, ARM=None):
    students = Students.objects.filter().order_by('gpa')[0:3]

    dataResponse = {
        "ARM": StudentsSerializer(instance=students, many=True).data
    }

    return Response(dataResponse)

