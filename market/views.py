from django.shortcuts import render
from .serializers import MarketSerailizer
from .models import MarketModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])
def market_view(request):
    if request.method=='GET':
        markets=MarketModel.objects.all()
        serializer=MarketSerailizer(markets,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=MarketSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['PUT','DELETE','GET','PATCH'])

def market_details(request,pk):
    try:
        market=MarketModel.objects.get(pk=pk)
    except MarketModel.DoesNotExist:
        return Response({'error':'Market not found'})
    if request.method=='GET':
        serializer=MarketSerailizer(market)
        return Response(serializer.data)
    if request.method in ['PUT','PATCH']:
        serializer=MarketSerailizer(market,data=request.data,partial=True if request.method =='PATCH' else False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method=='DELETE':
        market.delete()
        return Response({'message':'Market deleted successfully'})