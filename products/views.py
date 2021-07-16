from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Print_Media, Digital_Media

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    print_media = Print_Media.objects.all()
    digital_media = Digital_Media.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')

            products = products.filter(category__name__in=categories)
            print_media = print_media.filter(name__in=categories)
            digital_media = digital_media.filter(name__in=categories)

            categories = Category.objects.filter(name__in=categories)
            # categories = Category.objects.filter(name__icontains=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'print_media': print_media,
        'digital_media': digital_media,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    print_media = Print_Media.objects.all()
    digital_media = Digital_Media.objects.all()
    media_type = Category.MEDIA_TYPE

    product = get_object_or_404(Product, pk=product_id)

    """ Setting the 'is_print_media' boolean in Product model
    for media that is printable so that the template can render
    the appropriate sizes to the customer """

    dm = ['icon_sets', 'brand_logos', 'web_banners', 'digital_media', 'sale_items', 'new_stock']
    pm = Product.objects.exclude(category__name__in=dm)
    for item in pm:
        item.is_print_media = True
        item.save()

    all_items = Product.objects.all()
    for item in all_items:
        if(item.name == 'business card' or (item.name == 'business card' and item.category.name == 'sale_items')
            or item.name == 'flyer' or (item.name == 'flyer' and item.category.name == 'sale_items')
                or item.name == 'poster' or (item.name == 'poster' and item.category.name == 'sale_items')):
            item.is_print_media = True
            item.save()
        elif(item.name == 'icon set' or (item.name == 'icon set' and item.category.name == 'sale_items')
                or item.name == 'brand logo' or (item.name == 'brand logo' and item.category.name == 'sale_items')
                or item.name == 'web banner' or (item.name == 'web banner' and item.category.name == 'sale_items')):
            item.is_print_media = False
            item.save()

    # print(Product.objects.filter(is_print_media=True))

    print('Print Media = ', product.is_print_media)

    context = {
        'product': product,
        'print_media': print_media,
        'digital_media': digital_media,
        'category_choices': Print_Media.CATEGORY_CHOICES,
        'size_choices': Print_Media.SIZE_CHOICES,
        'media_type': Category.MEDIA_TYPE,
    }
    return render(request, 'products/product_detail.html', context)
