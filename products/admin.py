from django.contrib import admin
from .models import Product, Category, Print_Media, Digital_Media, MediaType

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
        'media_type',
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

class MediaTypeAdmin(admin.ModelAdmin):

    list_display = (
        'media_type',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Print_Media, Print_MediaAdmin)
admin.site.register(Digital_Media, Digital_MediaAdmin)
admin.site.register(MediaType, MediaTypeAdmin)
