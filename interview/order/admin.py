from django.contrib import admin
from .models import Order, OrderTag
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'embargo_date')
    list_filter = ('start_date', 'embargo_date')
    search_fields = ('start_date', 'embargo_date')

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderTag)
