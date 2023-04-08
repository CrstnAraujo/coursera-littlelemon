from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSeralizer

# Create your views here.
class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSeralizer


class SingleMenuItemView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSeralizer


@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})