from django.contrib import admin
from . models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ["Name", "Email", "Phone"]
    list_filter = ["Service"]
    search_fields = ["Email"]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)
