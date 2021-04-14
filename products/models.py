from django.db import models


class Print_Media(models.Model):

    class Meta:
        verbose_name_plural = 'Print Media'

    CATEGORY_CHOICES = (
        ('business_cards', 'Business Cards'),
        ('leaflets_flyers', 'Leaflets & Flyers'),
        ('posters', 'Posters')
    )
    name = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="Print Media")

    SIZE_CHOICES = (
        ('3.5x2', '3.5 x 2 inches'),
        ('2x3.5', '2 x 3.5 inches'),
        ('11x8.5', '11 x 8.5 inches'),
        ('8.3x5.8', '8.3 x 5.8 inches'),
        ('5.8x4.1', '5.8 x 4.1 inches'),
        ('8.3x3.9', '8.3 x 3.9 inches'),
    )
    size = models.CharField(max_length=20, choices=SIZE_CHOICES, default="Size")

    def __str__(self):
        return self.name


class Digital_Media(models.Model):

    class Meta:
        verbose_name_plural = 'Digital Media'

    CATEGORY_CHOICES = (
        ('icon_sets', 'Icon Sets'),
        ('brand_logos', 'Brand Logos'),
        ('web_banners', 'Web Banners')
    )
    name = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="Digital_Media")

    SIZE_CHOICES = (
        ('1616', '16 x 16 pixels'),
        ('3232', '32 x 32 pixels'),
        ('6464', '64 x 64 pixels'),
        ('128128', '128 x 128 pixels'),
        ('256256', '256 x 256 pixels')
    )
    size = models.CharField(max_length=20, choices=SIZE_CHOICES, default="Size")

    def __str__(self):
        return self.name


class MediaType(models.Model):

    MEDIA_TYPE = (
        ('print_media', 'Print Media'),
        ('digital_media', 'Digital Media'),
    )
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPE, null=False)

    def __str__(self):
        return self.media_type


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    MEDIA_TYPE = (
        ('print_media', 'Print Media'),
        ('digital_media', 'Digital Media'),
    )
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPE, null=False, default='print_media')

    def __str__(self):
        return self.media_type

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    is_print = models.BooleanField(null=False, default=True)
    is_digital = models.BooleanField(null=False, default=False)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
