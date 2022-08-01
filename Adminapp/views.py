from django.http import JsonResponse
from django.shortcuts import render
from .serializer import *
from rest_framework.views import APIView

class RegistrationAPI(APIView):
    def post(self,request, *args, **kwargs):
        try:
            Data = request.data
            serializer = RegisterUserSerializer(data=Data)
            if serializer.is_valid():
                serializer.save()
            return JsonResponse({"message":"Registration successfully"},safe=False,status=200)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)

