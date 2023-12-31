"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from record import views
from record.views import (
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    OrderListView, OrderCreateView, OrderUpdateView, OrderDeleteView,
    OrderItemListView, OrderItemCreateView, OrderItemUpdateView, OrderItemDeleteView,
    ReviewListView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),

    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/add/', ProductCreateView.as_view(), name='product-add'),
    path('product/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/add/', CategoryCreateView.as_view(), name='category-add'),
    path('categories/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('order/add/', OrderCreateView.as_view(), name='order-add'),
    path('order/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
    
    path('orderitems/', OrderItemListView.as_view(), name='orderitem-list'),
    path('orderitems/add/', OrderItemCreateView.as_view(), name='orderitem-add'),
    path('orderitems/<int:pk>/', OrderItemUpdateView.as_view(), name='orderitem-update'),
    path('orderitems/<int:pk>/delete/', OrderItemDeleteView.as_view(), name='orderitem-delete'),
    
    path('review/', ReviewListView.as_view(), name='review-list'),
    path('review/add/', ReviewCreateView.as_view(), name='review-add'),
    path('reviews/<int:pk>/', ReviewUpdateView.as_view(), name='review-update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

