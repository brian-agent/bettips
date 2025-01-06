from rest_framework.serializers import ModelSerializer
from .models import Fixture
from django_countries.fields import CountryField
from rest_framework import serializers
class FixtureSerializer(ModelSerializer):
    country= serializers.SerializerMethodField()
    class Meta:
        model = Fixture
        fields = '__all__'
    def get_country(self, obj):
        return obj.country.name
# Compare this snippet from bettips/api/urls.py: