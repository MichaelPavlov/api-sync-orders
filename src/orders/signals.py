import requests
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rest_framework.reverse import reverse

from orders import serializers
from orders.models import Order


@receiver(post_save, sender=Order)
def order_post_save(instance, created, **kwargs):
    data = serializers.OrderSerializer(instance).data
    if created:
        url = reverse("orders:order-list")
        url = settings.MIRROR_URI + url
        requests.post(url, data=data)
    else:
        url = reverse("orders:order-detail", kwargs={"uuid": data.pop("uuid")})
        url = settings.MIRROR_URI + url
        requests.put(url, data=data)


@receiver(post_delete, sender=Order)
def order_post_delete(instance, **kwargs):
    data = serializers.OrderSerializer(instance).data
    url = reverse("orders:order-detail", kwargs={"uuid": data.pop("uuid")})
    url = settings.MIRROR_URI + url
    requests.delete(url)
