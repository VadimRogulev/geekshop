from django import template
from django.conf import settings

register = template.Library()


def media_for_products(image):
    if not image:
        image = 'products_images/product-1.jpg'

    return f'{settings.MEDIA_URL}{image}'


@register.filter(name='media_for_users')
def media_for_users(avatar):

    if not avatar:
        avatar = 'users/rv2v4F_xVbc.jpg'

    return f'{settings.MEDIA_URL}{avatar}'


register.filter('media_for_products', media_for_products)