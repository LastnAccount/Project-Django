import random
from faker import Faker
from django.utils import timezone
from django.core.management.base import BaseCommand
from myapp.models import Product, Category, Order, OrderItem, Review

fake = Faker()

class Command(BaseCommand):

    help = 'Create initial data for the record models'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating initial data...'))

        # Create categories
        categories = []
        for _ in range(5):
            category = Category(
                name=fake.word(),
                description=fake.sentence()
            )
            category.save()
            categories.append(category)

        # Create products with categories
        products = []
        for _ in range(10):
            product = Product(
                name=fake.word(),
                description=fake.sentence(),
                price=random.uniform(5, 100),
                image=fake.image_url(),
                category=random.choice(categories)
            )
            product.save()
            products.append(product)

        # Create orders with order items
        orders = []
        for _ in range(5):
            order = Order(
                customer_name=fake.name(),
                email=fake.email(),
                total_amount=random.uniform(20, 200)
            )
            order.save()
            orders.append(order)

            for _ in range(random.randint(1, 5)):
                order_item = OrderItem(
                    product=random.choice(products),
                    order=order,
                    quantity=random.randint(1, 10)
                )
                order_item.save()

        # Create reviews for products
        reviews = []
        for product in products:
            for _ in range(random.randint(1, 3)):
                review = Review(
                    product=product,
                    user_name=fake.user_name(),
                    comment=fake.paragraph()
                )
                review.save()
                reviews.append(review)

        self.stdout.write(self.style.SUCCESS('Initial data created successfully.'))
