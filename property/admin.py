from django.contrib import admin

from .models import Complaint, Flat, Owner


class OwnersInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('owner',)

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'is_building_new', 'construction_year', 'town')
    list_editable = ('is_building_new',)
    raw_id_fields = ('liked_by',)
    list_filter = ('is_building_new', 'rooms_number', 'has_balcony')
    inlines = (OwnersInline,)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
