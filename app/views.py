from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def employeedata(request):
    EMPDATA=Employee.objects.all()
    EMPJSONDATA=EmployeeModelSerializers(EMPDATA,many=True)
    return Response(EMPJSONDATA.data)
