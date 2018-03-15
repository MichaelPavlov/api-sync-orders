from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from orders.models import Order


class OrderViewSetTest(APITestCase):
    def test_order_can_be_created(self):
        url = reverse("orders:order-list")
        data = {
            'quantity': 5,
            'total_price': 5555
        }
        response = self.client.post(url, data=data)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.first().quantity, 5)
        self.assertEqual(Order.objects.first().total_price, 5555)

    def test_order_can_be_updated(self):
        order = Order.objects.create(quantity=5, total_price=5555)
        url = reverse("orders:order-detail", kwargs={'pk': order.id})
        data = {
            'id': order.id,
            'quantity': 7,
            'total_price': 7777
        }
        response = self.client.put(url, data=data)
        order.refresh_from_db()
        self.assertEqual(order.quantity, data["quantity"])
        self.assertEqual(order.total_price, data["total_price"])

    def test_order_can_be_deleted(self):
        order = Order.objects.create(quantity=5, total_price=5555)
        url = reverse("orders:order-detail", kwargs={'pk': order.id})
        response = self.client.delete(url)
        self.assertEqual(Order.objects.count(), 0)
