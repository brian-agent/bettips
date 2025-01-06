from django.shortcuts import render
from .models import Fixture
from django.utils import timezone
from rest_framework.response import Response
from .serializer import FixtureSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import date

# Create your views here.
@api_view(['GET'])
def home(request):
    today = timezone.now().date()  # Use timezone-aware datetime for today
    fixtures = Fixture.objects.filter(created_at__date=today)  # Use __date lookup on DateTimeField
    
    serializer = FixtureSerializer(fixtures, many=True)
    return Response(serializer.data , status=status.HTTP_200_OK)
@api_view(['GET'])
def all_games(request):
    fixtures=Fixture.objects.all()
    serializer= FixtureSerializer(fixtures)
    return Response(serializer.data,status=status.HTTP_200_OK)