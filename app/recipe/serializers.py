"""
Serializers for recipe APIs
"""
from rest_framework import serializers

from app.core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe."""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']
