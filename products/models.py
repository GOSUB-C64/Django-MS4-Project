from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)

    def __str__(self):
        return self.first_name


class Print_Media(models.Model):

    class Meta:
        verbose_name_plural = 'Print Media'

    CATEGORY_CHOICES = (
        ('business_cards', 'Business Cards'),
        ('leaflets_flyers', 'Leaflets & Flyers'),
        ('posters', 'Posters')
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    SIZE_CHOICES = (
        ('3.5x2.0', '3.5 x 2 inches'),
        ('2x3.5', '2.0 x 3.5 inches'),
        ('11x8.5', '11 x 8.5 inches'),
        ('8.3x5.8', '8.3 x 5.8 inches'),
        ('5.8x4.1', '5.8 x 4.1 inches'),
        ('8.3x3.9', '8.3 x 3.9 inches'),
    )
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)

    def __str__(self):
        return self.category


class Digital_Media(models.Model):

    class Meta:
        verbose_name_plural = 'Digital Media'

    CATEGORY_CHOICES = (
        ('icon_sets', 'Icon Sets'),
        ('brand_logos', 'Brand Logos'),
        ('web_banners', 'Web Banners')
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    SIZE_CHOICES = (
        ('1616', '16 x 16 pixels'),
        ('3232', '32 x 32 pixels'),
        ('6464', '64 x 64 pixels'),
        ('128128', '128 x 128 pixels'),
        ('256256', '256 x 256 pixels')
    )
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)

    def __str__(self):
        return self.category
