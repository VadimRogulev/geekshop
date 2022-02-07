from django.db import models

from django.conf import settings
from mainapp.models import Product


class Order(models.Model):
    STATUS_FORMING = 'FM'
    STATUS_SENT_TO_PROCEED = 'STP'
    STATUS_PROCEEDED = 'PRD'
    STATUS_PAID = 'PD'
    STATUS_DONE = 'DN'
    STATUS_CANCEL = 'CNL'

    STATUSES = (
        (STATUS_FORMING, 'формируется'),
        (STATUS_SENT_TO_PROCEED, 'отправлен в обработку'),
        (STATUS_PAID, 'оплачен'),
        (STATUS_PROCEEDED, 'обрабатывается'),
        (STATUS_DONE, 'готов к выдаче'),
        (STATUS_CANCEL, 'отменен'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='обновлен', auto_now=True)
    status = models.CharField(verbose_name='статус', max_length=3, choices=STATUSES, default=STATUS_FORMING)
    is_active = models.BooleanField(verbose_name='активен', default=True)
#
#     class Meta:
#         ordering = ('-created',)
#         verbose_name = 'заказ'
#         verbose_name_plural = 'заказы'
#
#     def __str__(self):
#         return 'Текущий заказ: {}'.format(self.id)

    def get_total_quantity(self):
        _items = self.orderitems.select_related()
        _total_quantity = sum(list(map(lambda x: x.quantity, _items)))
        return _total_quantity
#
#     def get_product_type_quantity(self):
#         items = self.orderitems.select_related()
#         return len(items)

    def get_total_cost(self):
        _items = self.orderitems.select_related()
        _total_cost = sum(list(map(lambda x: x.quantity * x.product.price, _items)))
        return _total_cost
#
#     # переопределяем метод, удаляющий объект
#     def delete(self):
#         for item in self.orderitems.select_related():
#             item.product.quantity += item.quantity
#             item.product.save()
#
#         self.is_active = False
#         self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='заказ', on_delete=models.CASCADE, related_name='orderitems') # related_name="orderitems"
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)

    def get_product_cost(self):
        return self.product.price * self.quantity

    @staticmethod
    def get_item(pk):
        return OrderItem.objects.get(pk=pk)