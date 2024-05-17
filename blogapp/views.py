from django.shortcuts import render
from rest_framework import viewsets
from blogapp.models import Article
from .serializers import Articleserializer
from rest_framework.response import Response

# Create your views here.
class newsView(viewsets.ViewSet):
    def list(self, request):
        data = Article.objects.all()
        aserializer = Articleserializer(data,many=True)
        return Response(aserializer.data)