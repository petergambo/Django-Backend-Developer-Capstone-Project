from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .forms import BookingForm, LoginForm
from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from datetime import datetime
from django.shortcuts import render
import json

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @action(detail=False, methods=['get'])
    def reservations(self, request):
        date = request.GET.get('date', datetime.today().date())
        bookings = Booking.objects.filter(reservation_date=date)
        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def bookings(self, request):
        data = request.data
        exist = Booking.objects.filter(reservation_date=data['reservation_date'], reservation_slot=data['reservation_slot']).exists()
        if not exist:
            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 1}, status=status.HTTP_400_BAD_REQUEST)

# Other views remain unchanged.



# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')



def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'login.html', context)