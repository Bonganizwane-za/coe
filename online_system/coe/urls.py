from django.urls import path
from . import views

app_name='coe'
urlpatterns = [
    path('', views.index, name='index'),
    path('venue_list/', views.venue_list, name='venue_list'),
    path('venues_detail/<pk>/', views.venue_detail, name='venue_detail'),
    #path('venues/create/', views.venue_create, name='venue_create'),
    #path('venues/<pk>/update/', views.venue_update, name='venue_update'),
    #path('venues/<pk>/delete/', views.venue_delete, name='venue_delete'),
    path('bookings_list/', views.bookings_list, name='bookings_list'),
    path('booking_form/<pk>', views.booking_form, name='booking_form'),
    path('booking_detail/<booking_pk>/', views.booking_detail, name='booking_detail'),
    path('booking_update/<booking_pk>/', views.booking_update, name='booking_update'),
    path('booking_cancellation/<booking_pk>', views.booking_cancellation, name='booking_cancellation'),
     path('calendar/', views.calendar, name='calendar'),
    path('create_event/', views.create_event, name='create_event'),
]