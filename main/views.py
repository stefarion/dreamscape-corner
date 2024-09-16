from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import ProductEntry

def show_main(request):
    products = ProductEntry.objects.all()

    context = {
        'products': products
    }
    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)