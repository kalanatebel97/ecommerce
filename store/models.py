from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Category(models.Model):

    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Product(models.Model):

    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name, self.price,self.status,self.description,self.category_id)


class CustomUser(AbstractUser):

    mobile_no = models.IntegerField(null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)

    # def __str__(self):
    #     return self.mobile_no

class Cart(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)

    def __str__(self):
        return self.product.name



