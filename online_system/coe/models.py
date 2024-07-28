# models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

import datetime
now = datetime.datetime.now()
iso_string = now.isoformat()
print(iso_string)
default_value = str(iso_string)
print(default_value)

# Venue Model
class Venue(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    size = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Event Model
class Event(models.Model):
    name = models.CharField(max_length=255)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    purpose = models.CharField(max_length=255)
    num_attendees = models.IntegerField()
    contact_person = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    telephone_number = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Calendar(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class CalendarEvent(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    end_time = models.TimeField()
    end_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.event.name} - {self.start_date} to {self.end_date}"

# Resource Model
class Resource(models.Model):
    ROOM = 'Room'
    EQUIPMENT = 'Equipment'
    STAFF = 'Staff'
    RESOURCE_TYPE_CHOICES = [
        (ROOM, 'Room'),
        (EQUIPMENT, 'Equipment'),
        (STAFF, 'Staff'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=RESOURCE_TYPE_CHOICES)
    size = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Booking Model
class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    location = models.CharField(max_length=250)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.event.name} - {self.venue.name}"

# Walk-in Booking Model
class WalkInBooking(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    contact_person = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.venue.name}"

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Opportunity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Opportunities"

