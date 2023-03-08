from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from order.models import Order
from order.serializers import OrederSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrederSerializer
    permission_classes = [IsAuthenticated]
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class OrderConfirmAPIView(APIView):
    def get(self, request, code):
        order = get_object_or_404(Order, activation_code=code)

        if not order.is_confirm:
            order.is_confirm = True
            order.status = 'in_processing'
            order.save(update_fields=['is_confirm', 'status'])
            return Response({'message': 'Поздравляю, ваш заказ подтвержден!'}, status=status.HTTP_200_OK)
        return Response({'message': 'Заказ уже подтвержден!'}, status=status.HTTP_400_BAD_REQUEST)


