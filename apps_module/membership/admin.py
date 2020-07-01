from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'member_id',
        'first_name',
        'middle_name',
        'last_name',
        'gender',
        'phone_number_1',
        'phone_number_2',
        'date_added',
        'date_updated',
    ]

    class Meta:
        model = Member

