from django.contrib import admin
from members.models import Member

class MemberAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    fieldsets = (
        (None, {
            'fields': (
                'title', 
                ( 'first_name', 'last_name'), 
                ('rotary_position', 'profession'),
                'profile_picture',
                'bio',
                'active',
                ('registration_date', 'resignation_date'),
            )
        }),
    )

admin.site.register(Member, MemberAdmin)