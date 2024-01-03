from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'menu', views.MenuViewSet)
router.register(r'booking', views.BookingViewSet)

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('bookings/', views.bookings, name='bookings'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),  # Make sure 'obtain_auth_token' is imported

    # Include DRF's router URLs
    path('api/', include(router.urls)),
]
