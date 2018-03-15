import uuid as uuid

from django.db import models


class Order(models.Model):
    # product = models.ForeignKey(Product)
    quantity = models.IntegerField(null=False, blank=False)
    total_price = models.IntegerField(null=False, blank=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return "#{}, goods quantity: {}, total price: {}".format(self.id, self.quantity, self.total_price)
