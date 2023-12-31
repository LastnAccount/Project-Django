# myapp/forms.py
from django.forms import ModelForm
from django import forms
from .models import Product, Category, Order, OrderItem, Review

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = "__all__"

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
