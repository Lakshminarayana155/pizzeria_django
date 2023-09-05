from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PizzaOrder
from .serializers import PizzaOrderSerializer

class PizzaOrderAPIView(APIView):
    def post(self, request):
        order_data_list = request.data  # Assuming you receive a list of orders

        # List to store created order instances
        created_orders = []

        for order_data in order_data_list:
            serializer = PizzaOrderSerializer(data=order_data)
            if serializer.is_valid():
                # Valid data, create the PizzaOrder instance
                order = serializer.save()
                created_orders.append(order)
            else:
                # If any order data is invalid, return a 400 response
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Return a 201 response with data for all created orders
        return Response(PizzaOrderSerializer(created_orders, many=True).data, status=status.HTTP_201_CREATED)
    
    # def post(self, request):
    #     serializer = PizzaOrderSerializer(data=request.data)
    #     if serializer.is_valid():
    #         # Valid data, create the PizzaOrder instance
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
