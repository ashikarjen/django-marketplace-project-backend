from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from rest_framework import generics
from .serializers import ProductSerializer

class ProductsListAPIView(generics.ListAPIView):
    """
    endpoint api/products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Create a new product instance
            product = form.save(commit=False)
            # Set the seller to the currently logged-in user
            product.seller = request.user
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})
