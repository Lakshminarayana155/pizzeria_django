from rest_framework import serializers
from .models import PizzaOrder, Topping

class PizzaOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaOrder
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Convert base and cheese IDs to their human-readable values
        data['base'] = dict(PizzaOrder.BASE_CHOICES)[data['base']]
        data['cheese'] = dict(PizzaOrder.CHEESE_CHOICES)[data['cheese']]
        # Fetch the names of toppings associated with their IDs
        topping_ids = data['toppings']
        data['toppings'] = [Topping.objects.get(id=topping_id).name for topping_id in topping_ids]

        return data
    
    def validate(self, data):
        # Validate that exactly 1 base, 1 cheese, and 5 toppings are chosen
        base = data.get('base')
        cheese = data.get('cheese')
        toppings = data.get('toppings')

        if not (base and cheese and toppings):
            raise serializers.ValidationError("Please choose 1 base, 1 cheese, and 5 toppings.")

        if len(toppings) != 5:
            raise serializers.ValidationError("Please choose exactly 5 toppings.")

        return data
