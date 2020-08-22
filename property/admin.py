from django.contrib import admin

from .models import Flat, Complain


class FlatAdmin(admin.ModelAdmin):
    list_display = ['address', 'price',
                    'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    search_fields = ['town', 'address', 'owner', 'new_building']
    readonly_fields = ['created_at']
    list_filter = ('new_building', 'rooms_number', 'has_balcony')


class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complain, ComplainAdmin)
