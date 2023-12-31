
from django.contrib import admin
from .models import Product, Category, Order, OrderItem, Review

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "created_at", "updated_at")
    search_fields = ("name", "description")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description","created_at", "updated_at")
    search_fields = ("name", "description")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_id", "customer_name", "email", "total_amount", "created_at", "updated_at")
    search_fields = ("customer_name", "email")

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("product", "order", "quantity", "created_at", "updated_at")
    search_fields = ("product__name", "order__customer_name")

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user_name", "comment", "created_at", "updated_at")
    search_fields = ("product__name", "user_name")
