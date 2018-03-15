from django.db.models.signals import post_save, post_delete, pre_init, post_init
from django.dispatch import receiver

from orders.models import Order

@receiver(post_save, sender=Order)
def order_post_save(sender, instance, created, **kwargs):
    print('post_save receiver')
    sender
    pass
    # order = instance.as_dict()
    #
    # url = settings.MIRROR_URI
    #
    # if created:
    #     url = reverse_lazy("order:create")
    #     url = mirror_server + url
    #     requests.post(url, order)
    # else:
    #     url = reverse_lazy("order:update")
    #     url = mirror_server + url
    #     requests.put(url, order)


@receiver(post_init, sender=Order)
def order_post_init(sender, instance, created, **kwargs):
    pass

@receiver(post_delete, sender=Order)
def order_post_delete(sender, instance, **kwargs):
    pass