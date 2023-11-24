from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET','POST'])
def employeedata(request):
    EMPDATA=Employee.objects.all()
    EMPJSONDATA=EmployeeModelSerializers(EMPDATA,many=True)
    return Response(EMPJSONDATA.data)