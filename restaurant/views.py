from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.generics import (
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class MenuItemView(ListCreateAPIView):
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]



