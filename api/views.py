from django.shortcuts import render
from .models import Fixture
from django.utils import timezone
from rest_framework.response import Response
from .serializer import FixtureSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import date
from datetime import timedelta

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
    serializer= FixtureSerializer(fixtures, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
def yesterday_games(request):
    yesterday = date.today() - timedelta(days=1)
    fixtures = Fixture.objects.filter(created_at__date=yesterday)
    serializer = FixtureSerializer(fixtures, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
def previous_two_days_games(request):
    two_days_ago = date.today() - timedelta(days=2)
    fixtures = Fixture.objects.filter(created_at__date=two_days_ago)
    serializer = FixtureSerializer(fixtures, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
def previous_three_days_games(request):
    three_days_ago = date.today() - timedelta(days=3)
    fixtures = Fixture.objects.filter(created_at__date=three_days_ago)
    serializer = FixtureSerializer(fixtures, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def previous_four_days_games(request):
    four_days_ago = date.today() - timedelta(days=4)
    fixtures = Fixture.objects.filter(created_at__date=four_days_ago)
    serializer = FixtureSerializer(fixtures, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)