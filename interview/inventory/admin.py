from django.contrib import admin
from .models import Inventory, InventoryTag, InventoryLanguage, InventoryType

# Register your models here.
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('type', 'language', 'tags', 'metadata')
    list_filter = ('type', 'language')

admin.site.register(Inventory, InventoryAdmin)
admin.site.register(InventoryTag)
admin.site.register(InventoryLanguage)
admin.site.register(InventoryType)
