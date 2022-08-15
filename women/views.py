from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, permissions
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Women
from .serializers import WomenSerializer

class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (permissions.IsAuthenticated,)

# class WomenList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class OneWomen(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

