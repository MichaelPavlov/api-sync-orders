from django.test import TestCase

from orders import models


class OrderPostSaveTest(TestCase):
    # @mock.patch(requests.post)
    def test_signal_fires_up_when_new_order_created(self):
        order = models.Order.objects.create(
            quantity=5,
            total_price=5555
        )
