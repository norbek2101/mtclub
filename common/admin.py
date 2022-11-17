from django.contrib import admin
from common.models import Sponsor, Student, University, Sponsorship

class SponsorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'id', 'phone_number',  'balance', 'spent_amount', 'organization', 'type', 'payment_type', 'status']
    list_editable = ['phone_number', 'type', 'payment_type', 'status']


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number',  'balance', 'contract', 'university', 'type')
    list_editable = ('full_name', 'phone_number', 'type', 'university')


class UniversityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']


class SponsorshipAdmin(admin.ModelAdmin):
    list_display = ['id', 'sponsor', 'student', 'amount']


admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Sponsorship, SponsorshipAdmin)