from django.shortcuts import render
from rest_framework import generics

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        start_date__gte = request.query_params.get('start_date__gte')
        embargo_date__lte = request.query_params.get('embargo_date__lte')
        orders = self.get_queryset()
        if start_date__gte is not None:
            orders.filter(start_date__gte=start_date__gte)
        if embargo_date__lte is not None:
            orders.filter(embargo_date__lte=embargo_date__lte)
        serializer = self.serializer_class(orders, many=True)
        
        return Response(serializer.data, status=200)
    
    def get_queryset(self):
        return self.queryset.all()

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer
