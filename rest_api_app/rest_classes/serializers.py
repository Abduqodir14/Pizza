# -*- coding: utf-8 -*-

from rest_framework import serializers

from pizza_auth_app.models import CustomUser
from pizza_app.models import PizzaMenuItem, PizzaIngredient


class PizzaMenuItemSerializer(serializers.HyperlinkedModelSerializer):

    ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=PizzaIngredient.objects.all())

    class Meta:
        model = PizzaMenuItem
        fields = ('id', 'name', 'ingredients')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id',
                  'username',
                  'email',
                  'our_note',
                  'favourite_pizza',
                  )
        favourite_pizza = PizzaMenuItemSerializer(required=False)
