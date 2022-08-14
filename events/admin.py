from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', )
    fieldsets = (
        (None, {
            'fields': ('slug','title', 'thumbnail', 'description', 'date', 'added_by')
        }),
        ('Address', {
            'fields': ('venue', 'street', 'suburb', 'town', 'postal_code')
        }),
        (None, {
            'fields': ('published', )
        })
    )


admin.site.register(Event, EventAdmin)