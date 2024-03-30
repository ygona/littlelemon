from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import Menu
from django.contrib.auth.models import User, Permission
from rest_framework.permissions import IsAuthenticated
from .serializers import MenuSerializer, UserSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer