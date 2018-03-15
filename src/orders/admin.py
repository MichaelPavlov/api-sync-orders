from django.contrib import admin

from orders.models import Order


class OrdersAdmin(admin.ModelAdmin):
    pass
    # fields = '__all__'


admin.site.register(Order, OrdersAdmin)
