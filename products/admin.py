from django.contrib import admin
from .models import Product, Category, Customer, Print_Media, Digital_Media

# Register your models here.


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'print_media',
        'digital_media',
    )


class CustomerAdmin(admin.ModelAdmin):

    list_display = (
        'first_name',
        'last_name',
        'email',
        'phone',
    )


class Print_MediaAdmin(admin.ModelAdmin):

    list_display = (
        'media',
        'size'
    )

class Digital_MediaAdmin(admin.ModelAdmin):

    list_display = (
        'media',
        'size'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Print_Media, Print_MediaAdmin)
admin.site.register(Digital_Media, Digital_MediaAdmin)
