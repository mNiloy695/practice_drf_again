from rest_framework import serializers
from .models import MarketModel

from django.core.mail import send_mail
# class MarketSerailizer(serializers.Serializer):
#     name=serializers.CharField(max_length=20)
#     description=serializers.CharField(max_length=100)
#     location=serializers.CharField(max_length=100)
#     market_open=serializers.BooleanField(default=True)

#     def create(self,validated_data):
       
#         return  MarketModel.objects.create(**validated_data)
     
#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.location=validated_data.get('location',instance.location)
#         instance.market_open=validated_data.get('market_open',instance.market_open)
#         instance.save()

#         return instance

class MarketSerailizer(serializers.ModelSerializer):
    class Meta:
        model=MarketModel
        fields="__all__"

        #if want to not add specific fields
        #exclude=['id]

    def create(self,validated_data):
            market=super().create(validated_data)
            send_mail(
            subject='New Market Created',
            message=f"The market '{market.name}' has been created at location: {market.location}.",
            from_email='sendingemail695@gmail.com',  # Replace with your actual sender email
            recipient_list=['mniloy695@gmail.com'],  # Change to actual recipient(s)
            fail_silently=False,
          )

            return market