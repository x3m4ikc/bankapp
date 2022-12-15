from django.shortcuts import render
from rest_framework import viewsets, mixins, generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from wallet.models import Wallet, User, Transaction
from wallet.serializers import WalletSerializer, UserSerializer, TransactionSerializer, UserRegisterSerializer


class WalletViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    @api_view(['POST'])
    def create_auth(self, request):
        serialized = UserSerializer(data=request.DATA)
        if request.data['username'] in User.objects.all():
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        if serialized.is_valid():
            User.objects.create_user(
                serialized.init_data['username'],
                serialized.init_data['password']
            )
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.ListModelMixin,
                         GenericViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
