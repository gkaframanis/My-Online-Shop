from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    # We retrieve only available products
    products = Product.objects.filter(available=True)
    # We can optionally filter products by category
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {"category": category, "categories": categories, "products": products}
    return render(request, "shop/product/list.html", context)


def product_detail(request, id, slug):
    # We get the product instance and we also use the slug to get it to build SEO friendly urls for products.
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {"product": product}
    return render(request, "shop/product/detail.html", context)
