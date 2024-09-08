from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Firefly Doll',
        'price': '850000',
        'description': 'Elevate your collection with the Honkai: Star Rail Firefly Doll!',
        'category': 'Plush'
    }

    return render(request, "main.html", context)