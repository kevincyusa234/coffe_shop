from django.contrib import admin

# Register your models here.
from .models import Booking, Product, Category, MenuItem

admin.site.register(Booking)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(MenuItem)


