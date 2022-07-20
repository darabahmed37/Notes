from rest_framework import serializers

from .models import Category, Notes


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id',)


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        exclude = ('id',)
        expandable_fields = {
            "category": CategorySerializer
        }
