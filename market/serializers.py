from rest_framework import serializers
from .models import MarketModel


class MarketSerailizer(serializers.Serializer):
    name=serializers.CharField(max_length=20)
    description=serializers.CharField(max_length=100)
    location=serializers.CharField(max_length=100)
    market_open=serializers.BooleanField(default=True)

    def create(self,validated_data):
       
        return  MarketModel.objects.create(**validated_data)
     
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.location=validated_data.get('location',instance.location)
        instance.market_open=validated_data.get('market_open',instance.market_open)
        instance.save()

        return instance