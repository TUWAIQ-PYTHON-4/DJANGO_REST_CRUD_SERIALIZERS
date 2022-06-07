from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
# Create your views here.
from .models import Students
from .seri import StudentSeri


@api_view(['POST'])
def add_stu(request : Request):
    new_stu = StudentSeri(data=request.data)
    if new_stu.is_valid():
        new_stu.save()
        dataResponse = {
            "msg": "Created Successfully",
            "stu": new_stu.data
        }
        return Response(dataResponse)
    else:
        print(new_stu.errors)
        dataResponse = {"msg": "couldn't create a student"}
        return Response(dataResponse)

@api_view(['GET'])
def list_stu(request:Request):
    stu = Students.objects.all()

    dataResponse = {
        "msg": "List of All students",
        "students": StudentSeri(instance=stu, many=True).data
    }

    return Response(dataResponse)

@api_view(['PUT'])
def put_stu(request:Request , stu_id):
    stu = Students.objects.get(id=stu_id)

    putStu = StudentSeri(instance=stu, data=request.data)
    if putStu.is_valid():
        putStu.save()
        responseData = {
            "msg": "updated successefully"
        }

        return Response(responseData)
    else:
        print(putStu.errors)
        return Response({"msg": "bad request, cannot update"})

@api_view(['DELETE'])
def delete_stu (request:Request , stu_id):
    stu = Students.objects.get(id=stu_id)
    stu.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['GET'])
def order (request : Request):
    order_stu = Students.objects.order_by('-GBA')
    dataResponse = {
        "msg": " Top 3 students",
        "students": StudentSeri(instance=order_stu[:3], many=True).data
    }
    return Response(dataResponse)

@api_view(['GET'])
def search(request: Request, stu_name):
    search  = Students.objects.filter(f_name__contains=stu_name)
    dataResponse = {
        'msg': "Student found" if search else "Student not found",
        "students": StudentSeri(instance=search, many=True).data
    }
    return Response(dataResponse)






