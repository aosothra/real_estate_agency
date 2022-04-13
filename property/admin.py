from django.contrib import admin

from .models import Complaint, Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'is_building_new', 'construction_year', 'town')
    list_editable = ('is_building_new',)
    raw_id_fields = ('liked_by',)
    list_filter = ('is_building_new', 'rooms_number', 'has_balcony')

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)