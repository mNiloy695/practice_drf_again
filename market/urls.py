from django.urls import path
from .views import market_view,market_details


urlpatterns = [
    path('list/',market_view,name='market-list'),
    path('<int:pk>/',market_details,name='market'),
]
