from django.shortcuts import render

# Create your views here.
# Les views ici sont des endpoint d'API
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserCreateSerializer, UserUpdateSerializer, UserResponseSerializer
from .services import UserService

user_service = UserService()

@api_view(['GET', 'POST'])
def user_list(request):
    """Liste tous les utilisateurs ou crée un nouvel utilisateur"""
    
    if request.method == 'GET':
        users = user_service.obtenir_tous_utilisateurs()
        serializer = UserResponseSerializer(users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = user_service.creer_utilisateur(serializer.validated_data)
                response_serializer = UserResponseSerializer(user)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def user_detail(request, pk):
    """Récupère, met à jour ou supprime un utilisateur"""
    
    if request.method == 'GET':
        user = user_service.obtenir_utilisateur(pk)
        if not user:
            return Response({'detail': 'Utilisateur non trouvé'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserResponseSerializer(user)
        return Response(serializer.data)
    
    elif request.method in ['PUT', 'PATCH']:
        serializer = UserUpdateSerializer(data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            try:
                user = user_service.mettre_a_jour_utilisateur(pk, serializer.validated_data)
                if not user:
                    return Response({'detail': 'Utilisateur non trouvé'}, status=status.HTTP_404_NOT_FOUND)
                response_serializer = UserResponseSerializer(user)
                return Response(response_serializer.data)
            except ValueError as e:
                return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        success = user_service.supprimer_utilisateur(pk)
        if not success:
            return Response({'detail': 'Utilisateur non trouvé'}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
