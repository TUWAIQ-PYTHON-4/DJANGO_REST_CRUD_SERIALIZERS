from django.shortcuts import render
from os import stat
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer


@api_view(["POST"])
def add_stu(request: Request):
    pass

    new_stu = StudentSerializer(data=request.data)
    if new_stu.is_valid():
        new_stu.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "student" : new_stu.data
        }
        return Response(dataResponse)
    else:
        print(new_stu.errors)
        dataResponse = {"msg" : "can't create a student"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def edit_stu(request: Request, std_id):
    std = Student.objects.get(id = std_id)

    updated_std = StudentSerializer(instance=std, data=request.data)
    if updated_std.is_valid():
        updated_std.save()
        responseData = {
            "msg": "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_std.errors)
        return Response({"msg": "can't update"}, status=status.HTTP_400_BAD_REQUEST)




@api_view(["GET"])
def list_stu(request: Request):
    std = Student.objects.all()

    dataResponse = {
        "msg": "List of All students",
        "students": StudentSerializer(instance=std, many=True).data
    }

    return Response(dataResponse)



@api_view(["DELETE"])
def del_stu(request : Request, std_id):
        std = Student.objects.get(id=std_id)
        std.delete()
        return Response({"msg": "Deleted Successfully"})





@api_view(['GET'])
def list_top(request: Request):
    top = Student.objects.all().sorted('gpa')[0:3]

    dataResponse = {
        "msg": "the list for 3 top students ",
        "student": StudentSerializer(instance=top, many=True).data
    }
    return Response(dataResponse)



@api_view(['GET'])
def search_stu(request: Request, name):
    std = Student.objects.filter(first_name=name)
    dataResponse = {
        "msg": "Search :",
        "student": StudentSerializer(instance=std, many=True).data
    }
    return Response(dataResponse)


