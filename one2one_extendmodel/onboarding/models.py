from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Seller(models.Model):
    class Meta:
        db_table='seller_info'

    user = models.OneToOneField(User)
    INDIVIDUAL = 'IND'
    DEALER = 'DEA'
    TYPE_OF_SELLER = (
        (INDIVIDUAL, 'Individual'),
        (DEALER, 'Dealer'),
    )

    seller_type = models.CharField(max_length=3,
                                   choices=TYPE_OF_SELLER,
                                   default=INDIVIDUAL)
    shop_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100, null=False)