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

    product = get_object_or_404(Product, pk=product_id)

    print(product, print_media, digital_media)
    context = {
        'product': product,
        'print_media': print_media,
        'digital_media': digital_media,
    }
    return render(request, 'products/product_detail.html', context)
