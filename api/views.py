from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PizzaOrder,Topping
from .serializers import PizzaOrderSerializer

class PizzaOrderAPIView(APIView):
    def get(self, request,id):
        try:
            order = PizzaOrder.objects.get(id=id)
        except PizzaOrder.DoesNotExist:
            return Response(
                {"error": "Pizza order not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PizzaOrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        existing_toppings_count = Topping.objects.count()

        if existing_toppings_count < 7:
            # Create the missing toppings
            required_toppings = ['Pepperoni','Mushrooms','Green Peppers','Onions','Black Olives','Sausage','Pineapple']
            for topping_name in required_toppings:
                Topping.objects.get_or_create(name=topping_name)
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
    
    
