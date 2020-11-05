from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request, 'carts/cart.html')

def order(request):
    return render(request, 'carts/order.html')
