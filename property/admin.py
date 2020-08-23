from django.contrib import admin

from .models import Flat, Complain, Owner


class FlatAdmin(admin.ModelAdmin):
    list_display = ['address', 'price',
                    'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    search_fields = ['town', 'address', 'owner', 'new_building']
    readonly_fields = ['created_at']
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)


class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user')

class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    raw_id_fields = ('flats',)



admin.site.register(Flat, FlatAdmin)
admin.site.register(Complain, ComplainAdmin)
admin.site.register(Owner, OwnerAdmin)
