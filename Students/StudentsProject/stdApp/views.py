from django.shortcuts import render
from os import stat
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import StudentModel
from .serializers import StudentSerializer
# Create your views here.
@api_view(['POST'])
def add_std(request : Request):
    new_std = StudentSerializer(data=request.data)
    if new_std.is_valid():
        new_std.save()
        STDdata = {
            "message" : "Created Successfully , Done ",
            "Student" : new_std.data
        }
        return Response(STDdata)
    else:
        print(new_std.errors)
        STDdata = {"message" : "Sorry, this student cannot be created !!"}
        return Response(STDdata , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def std_list(request : Request):
    stds = StudentModel.objects.all()

    STDdata = {
        "message": "Students",
        "Students" : StudentSerializer(instance=stds , many=True).data
    }
    return Response(STDdata)

@api_view(['PUT'])
def update_stds_info(request : Request, std_id):
    std = StudentModel.objects.get(id = std_id)
    edit_std = StudentSerializer(instance=std ,data=request.data)
    if edit_std.is_valid():
        edit_std.save()
        STDdata ={
            "message": "updated successefully"
        }
        return Response(STDdata)
    else:
        print(edit_std.errors)
        return Response( {"message":"bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_std(request: Request, std_id):
    city = StudentModel.objects.get(id=std_id)
    city.delete()
    return Response({"message": "Deleted Successfully"})


@api_view(['GET'])
def top_studenrs(request: Request):
    stds = StudentModel.objects.order_by('GPA')
    list_stds = StudentSerializer(instance=stds , many=True).data

    STDdata = {"Top_Student": list_stds[-3:]}
    return Response(STDdata)

@api_view(['GET'])
def search_name(request: Request, std_name):
    student = StudentModel.objects.filter(first_name=std_name)
    STDdata = {
        "message": "write the name you would search about it :",
        "student Name": StudentSerializer(instance=student, many=True).data
    }
    return Response(STDdata)


