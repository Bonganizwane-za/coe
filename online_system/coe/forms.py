# forms.py
from django import forms
from .models import Venue, Event, Resource, Booking

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'location', 'size', 'price')  # Add the fields you want to include in the form

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'location', 'purpose', 'num_attendees', 'contact_person')  # Add the fields you want to include in the form

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ('name', 'type', 'size', 'location')  # Add the fields you want to include in the form

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('venue',)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'venue', 'num_attendees', 'contact_person', 'telephone_number')