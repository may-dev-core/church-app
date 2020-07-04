from django.contrib import admin
from .models import Member, Attendance


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        # 'id',
        'member_id',
        'first_name',
        'middle_name',
        'last_name',
        'gender',
        'phone_number_1',
        'phone_number_2',
        'new_comer',
        'date_added',
        'date_updated',
    ]

    # fields = ('first_name',
    #           'middle_name',
    #           'last_name',
    #           'gender',
    #           'phone_number_1',
    #           'phone_number_2', )
    # readonly_fields = ('member_id',)

    date_hierarchy = 'date_added'
    # list_editable = ('first_name', 'middle_name', 'last_name', 'gender', 'phone_number_1',
    #                  'phone_number_2',)
    # list_filter = ('member_id', 'first_name',
    #                'middle_name', 'last_name', 'date_added')
    search_fields = ('member_id', 'first_name',
                     'middle_name', 'last_name',)
    list_per_page = 200
    list_max_show_all = 500

    def get_form(self, request, obj=None, **kwargs):
        try:
            form = super(MemberAdmin, self).get_form(request, obj, **kwargs)
            form.base_fields['member_id'].initial = self.member_id = int(Member.objects.order_by(
                'member_id').last().member_id) + 1
            form.base_fields['member_id'].editable = False
        except Exception as identifier:
            self.member_id = 1001

        return form

    # readonly_fields = ('member_id',)
    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)

    #     try:
    #         pass
    #     except expression as identifier:
    #         pass

    class Meta:
        model = Member


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    autocomplete_fields = ['member']

    def member_id(self, obj):
        return f'{obj.member.member_id}'

    def member_name(self, obj):
        return f'{obj.member.last_name} {obj.member.first_name}'

    list_display = [
        'date',
        'member_id',
        'member_name',
        # 'temp_tens',
        # 'temp_ones',
        # 'temp_decimals',
        'temperature',
        'present',
        'child',
        'date_added'
    ]

    fields = (
        'date',
        'member',
        # 'present',
        ('temp_tens', 'temp_ones', 'temp_decimals'),
        'child',


    )

    # readonly_fields = ('temperature',)
    date_hierarchy = 'date'
    search_fields = ('member__member_id',
                     'member__first_name', 'member__last_name')
    list_filter = ('date',)
    list_display_links = ['member_id', 'member_name']

    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)

    class Meta:
        model = Attendance


class AttendanceInline(admin.TabularInline):
    model = Attendance
    # exclude = ['short_description']
