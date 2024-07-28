from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Venue, Event, Resource, Booking, WalkInBooking, Opportunity 
from .forms import VenueForm, EventForm, ResourceForm, BookingForm
from django.contrib import messages
from .forms import EventForm

def index(request):
    return render(request, 'coe/index.html')

# Venue views
def venue_list(request):
    venues = Venue.objects.all()
    context = {'venues': venues}
    return render(request, 'coe/venue_list.html', context)

def venue_detail(request, pk):
    venue = Venue.objects.get(pk=pk)
    return render(request, 'coe/venue_detail.html', {'venue': venue})

def venue_create(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venue_list')
    else:
        form = VenueForm()
    return render(request, 'coe/venue_form.html', {'form': form})

def venue_update(request, pk):
    venue = Venue.objects.get(pk=pk)
    if request.method == 'POST':
        form = VenueForm(request.POST, instance=venue)
        if form.is_valid():
            form.save()
            return redirect('venue_list')
    else:
        form = VenueForm(instance=venue)
    return render(request, 'coe/venue_form.html', {'form': form})

def venue_delete(request, pk):
    venue = Venue.objects.get(pk=pk)
    if request.method == 'POST':
        venue.delete()
        return redirect('venue_list')
    return render(request, 'coe/venue_confirm_delete.html', {'venue': venue})

# Event views
def event_list(request):
    events = Event.objects.all()
    return render(request, 'coe/event_list.html', {'events': events})

def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, 'coe/event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'coe/event_form.html', {'form': form})

def event_update(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'coe/event_form.html', {'form': form})

def event_delete(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'coe/event_confirm_delete.html', {'event': event})

# Resource views
def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'coe/resource_list.html', {'resources': resources})

def resource_detail(request, pk):
    resource = Resource.objects.get(pk=pk)
    return render(request, 'coe/resource_detail.html', {'resource': resource})

def resource_create(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
    else:
        form = ResourceForm()
    return render(request, 'coe/resource_form.html', {'form': form})

def resource_update(request, pk):
    resource = Resource.objects.get(pk=pk)
    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
    else:
        form = ResourceForm(instance=resource)
    return render(request, 'coe/resource_form.html', {'form': form})

def resource_delete(request, pk):
    resource = Resource.objects.get(pk=pk)
    if request.method == 'POST':
        resource.delete()
        return redirect('resource_list')
    return render(request, 'coe/resource_confirm_delete.html', {'resource': resource})

# Booking views
def bookings_list(request):
    bookings = Booking.objects.all()
    return render(request, 'coe/bookings_list.html', {'bookings': bookings})

def booking_detail(request, pk):
    booking = Booking.objects.get(pk=pk)
    return render(request, 'coe/booking_detail.html', {'booking': booking})

def booking_form(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == 'POST':
        booking = Booking(event=event, **request.POST)
        booking.save()
        return redirect('booking_success')
    return render(request, 'coe/booking_form.html', {'event': event})

def booking_update(request, pk):
    booking = Booking.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'coe/booking_update.html', {'form': form})

def booking_cancellation(request, venue_pk, booking_pk):
    venue = Venue.objects.get(pk=venue_pk)
    booking = Booking.objects.get(pk=booking_pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('bookings_list', venue_pk=venue_pk)
    return render(request, 'coe/booking_cancellation.html', {'venue': venue, 'booking': booking})

def booking_success(request):
    return render(request, 'coe/booking_success.html')  


def calendar(request):
    events = Event.objects.all()
    venues = Venue.objects.all()
    return render(request, 'coe/calendar.html', {'events': events, 'venues': venues})

def book_venue(request, venue_id, start_date, end_date):
    venue = Venue.objects.get(id=venue_id)
    events = Event.objects.filter(venue=venue, start_date__lte=end_date, end_date__gte=start_date)
    if events.exists():
        messages.error(request, 'Venue is already booked for this time period')
        return redirect('calendar')
    else:
        event = Event.objects.create(title='New Event', start_date=start_date, end_date=end_date, venue=venue)
        messages.success(request, 'Venue booked successfully')
        return redirect('coe/calendar')

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            venue_id = form.cleaned_data['venue']
            return book_venue(request, venue_id, start_date, end_date)
    else:
        form = EventForm()
    return render(request, 'coe/create_event.html', {'form': form})