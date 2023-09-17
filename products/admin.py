from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'seller', 'seller_phone')
    search_fields = ('name', 'seller__username')
    list_filter = ('seller',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.seller = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)