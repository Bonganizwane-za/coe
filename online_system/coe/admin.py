from django.contrib import admin

from .models import *

admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Resource)
admin.site.register(Booking)
admin.site.register(WalkInBooking)
admin.site.register(CalendarEvent)
admin.site.register(Calendar)
admin.site.register(Opportunity)
