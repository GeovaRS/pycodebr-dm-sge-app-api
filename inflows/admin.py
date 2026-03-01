from django.contrib import admin
from . import models


class InFlowAdmin(admin.ModelAdmin):
    list_display = (
        'supplier',
        'product',
        'quantity',
        'description',
        'created_at',
        'updated_at'
    )
    search_fields = ('product',)


admin.site.register(models.InFlow, InFlowAdmin)
