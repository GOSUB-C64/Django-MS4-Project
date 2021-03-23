from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view that renders items in shopping bag """

    return render(request, 'bag/bag.html')
