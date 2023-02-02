from django.contrib import admin

from itemise.models import Bill, Item


# Make your models available in the Django Admin interface here

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
