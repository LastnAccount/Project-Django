from django.shortcuts import render
# myapp/views.py
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from record.models import Product, Category, Order, OrderItem, Review
from record.forms import ProductForm, CategoryForm, OrderForm, OrderItemForm, ReviewForm
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = Category
    context_object_name = 'home'
    template_name = "base.html"
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       return context

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        return Product.objects.all()

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_add.html'
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_edit.html'
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_del.html'
    success_url = reverse_lazy('product-list')

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 5

    def get_queryset(self):
        return Category.objects.all()

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_add.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_edit.html'
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'order'
    paginate_by = 5

    def get_queryset(self):
        return Order.objects.all()

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_add.html'
    success_url = reverse_lazy('order-list')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_edit.html'
    success_url = reverse_lazy('order-list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_del.html'
    success_url = reverse_lazy('ordert-list')
    
class OrderItemListView(ListView):
    model = OrderItem
    template_name = 'orderItem_list.html'
    context_object_name = 'orderitem'
    paginate_by = 5

    def get_queryset(self):
        return OrderItem.objects.all()

class OrderItemCreateView(CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'orderItem_add.html'
    success_url = reverse_lazy('orderItem-list')

class OrderItemUpdateView(UpdateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'orderItem_edit.html'
    success_url = reverse_lazy('orderItem-list')

class OrderItemDeleteView(DeleteView):
    model = OrderItem
    template_name = 'orderItem_del.html'
    success_url = reverse_lazy('orderItem-list')

class ReviewListView(ListView):
    model = Review  # Use the correct model name
    template_name = 'review_list.html'
    context_object_name = 'review'
    paginate_by = 5

    def get_queryset(self):
        return Review.objects.all()

class ReviewCreateView(CreateView):
    model = Review
    form_class = OrderItemForm
    template_name = 'review_add.html'
    success_url = reverse_lazy('review-list')

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = OrderItemForm
    template_name = 'review_edit.html'
    success_url = reverse_lazy('review-list')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review_del.html'
    success_url = reverse_lazy('review-list')
    
# Similarly, create views for Order , OrderItem, and Review 
# models following the pattern above.
