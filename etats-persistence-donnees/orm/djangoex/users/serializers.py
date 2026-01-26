# Les serializers sont des DTO dans Django
from rest_framework import serializers
from .models import User

class UserCreateSerializer(serializers.Serializer):
    """Serializer pour créer un utilisateur - Input API"""
    email = serializers.EmailField()
    nom = serializers.CharField(max_length=100)
    prenom = serializers.CharField(max_length=100)
    age = serializers.IntegerField()


class UserUpdateSerializer(serializers.Serializer):
    """Serializer pour mettre à jour un utilisateur - Input API"""
    email = serializers.EmailField(required=False)
    nom = serializers.CharField(max_length=100, required=False)
    prenom = serializers.CharField(max_length=100, required=False)
    age = serializers.IntegerField(required=False)
    actif = serializers.BooleanField(required=False)


class UserResponseSerializer(serializers.ModelSerializer):
    """Serializer de réponse - Output API"""
    class Meta:
        model = User
        fields = ['id', 'email', 'nom', 'prenom', 'age', 'actif', 'date_creation']
        read_only_fields = ['id', 'date_creation']



