
from rest_framework import serializers
from .models import Emp

class EmpSerializer(serializers.ModelSerializer):
  class Meta:
    model = Emp
    fields = ['id','name', 'title', 'location', 'age', 'salary']
