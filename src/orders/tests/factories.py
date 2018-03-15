import factory
from faker import Faker

from orders.models import Order

faker = Faker()


class OrderFactory(factory.DjangoModelFactory):
    quantity = factory.Faker('pyint')
    total_price = factory.Faker('pyint')
    uuid = factory.Faker('uuid4')

    class Meta:
        model = Order
        django_get_or_create = ('uuid',)
