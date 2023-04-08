from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView 
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import MenuItem, Booking
from .serializers import UserSerializer ,MenuItemSeralizer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSeralizer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSeralizer


class BookingViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]