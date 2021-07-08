from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    digital_media_sizes = {'dm1':"16 x 16 pixels", 'dm2':"32 x 32 pixels", 'dm3':"64 x 64 pixels",
        'dm4':"128 x 128 pixels", 'dm5':"256 x 256 pixels"}
    print_media_sizes = {'pm1':"3.5 x 2 inches", 'pm2':"2 x 3.5 inches", 'pm3':"11 x 8.5 inches",
        'pm4':"8.3 x 5.8 inches", 'pm5':"5.8 x 4.1 inches", 'pm6':"8.3 x 3.9 inches",
            'pm_A1':"A1 - 33.1 x 23.4 inches", 'pm_A2':"A2 - 23.4 x 16.5 inches",
                'pm_A3':"A3 - 16.5 x 11.7 inches", 'pm_A4':"A4 - 11.7 x 8.3 inches"}

    context = {
        'digital_media_sizes': digital_media_sizes,
        'print_media_sizes': print_media_sizes,
    }
    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)

    # quantity = request.POST.get('quantity',False)
    quantity = int(request.POST.get('quantity'))
    print("QUANTITY =", quantity)

    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        print("PRODUCT_SIZE =", 'product_size', request.POST.get('product_size'))
        size = request.POST['product_size']
    
    bag = request.session.get('bag', {})

    if size:
        print("SIZE IS..... ", size)
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(f"BAG: {bag}")
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    product = get_object_or_404(Product, pk=item_id)

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)

    bag = request.session.get('bag', {})
    bag.pop(item_id)
    messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return HttpResponse(status=200)
