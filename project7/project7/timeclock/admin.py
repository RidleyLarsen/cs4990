from django.contrib import admin
from .models import Event, Volunteer


class VolunteerAdmin(admin.ModelAdmin):
    readonly_fields = (
        'total_hours',
    )
    list_display = (
        'name',
        'date',
        'active',
        'active_recently',
        'total_hours',
    )
    list_filter = (
        'active',
    )


class EventAdmin(admin.ModelAdmin):
    readonly_fields = (
        'duration',
    )
    list_display = (
        'user', 'time_in', 'time_out', 'duration'
    )
    list_filter = (
        'user',
    )

# Register your models here.
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Event, EventAdmin)
