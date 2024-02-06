from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


def index(request):
    return render(request, 'index.html', {})


class MenuListCreateApi(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class MenuRetrieveUpdateDestroyApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


router = DefaultRouter()
router.register(r'tables', BookingViewSet)
