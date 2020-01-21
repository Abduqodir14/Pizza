from django.contrib import admin
from pizza_app.models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "full", )


admin.site.register(Address, AddressAdmin)





