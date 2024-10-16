from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from .models import NumerologyData
from django.shortcuts import render
from .serializers import NumerologyDataSerializer



class NumerologyBulkCreateView(APIView):

    def get(self, request):
        numerology_data = NumerologyData.objects.all()
        serializer = NumerologyDataSerializer(numerology_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

def home(request):
    return render(request,'api_data.html')