from django.shortcuts import render
from rest_framework import generics

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer

class DeactivateOrderView(generics.APIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def patch(self, request: Request, *args, **kwargs) -> Response:
        orders = Order.objects.filter(id=kwargs['id'])
        if not orders:
            return Response(serializer.errors, status=400)
        orders.update(is_active=True)
        serializer = self.serializer_class(orders, data=orders, partial=True)

        serializer.save()
        
        return Response(serializer.data, status=200)
