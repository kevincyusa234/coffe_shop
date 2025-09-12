from django.shortcuts import render, redirect
from .models import Booking, Product, Category, MenuItem
# Create your views here.
def index(request):
    categories = Category.objects.all()

    # Build menu grouped by category
    menu_items = []
    for category in categories:
        items = MenuItem.objects.filter(category=category, status=True)
        if items.exists():  # only include if there are items
            menu_items.append({
                'category': category.name,
                'items': items
            })
            print(category.name, items[0].product.name)

    context = {
        'menu_items': menu_items,
        'categories': categories,
    }

    return render(request, 'index.html', context)

def reservation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        people = request.POST.get('people')
        comments = request.POST.get('comments')
        Booking.objects.create(
            name=name,
            phone=phone,
            date=date,
            time=time,
            people=people,
            comments=comments
        )
    
    return render(request, 'reservation.html')

def booking(request):
    
    return render(request, 'reservation.html')


