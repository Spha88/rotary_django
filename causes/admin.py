from django.contrib import admin
from .models import Cause

class CauseAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

admin.site.register(Cause, CauseAdmin)