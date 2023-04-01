from rest_framework import serializers
from .models import mymodel

class myappSerializer(serializers.ModelSerializer):
    class Meta:
        model = mymodel
        fields = [ 'title', 'content', 'user']