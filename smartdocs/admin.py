from django.contrib import admin
from .models import Product, Category, Document

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Document)