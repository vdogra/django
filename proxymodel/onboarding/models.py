from django.db import models


#Custom model managers

class StartsWithVManager(models.Manager):

    def get_queryset(self):
        return super(StartsWithVManager, self).get_queryset().filter(first_name__startswith='V')

# Proxy model example for a custom model
class Person(models.Model):
    class Meta:
        db_table = 'person_info'
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class MyPerson(Person):
    class Meta:
        ordering = ['last_name']
        proxy = True

class OrderedPersonFirstName(Person):
    class Meta:
        ordering = ['first_name']
        proxy = True

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class StartsWithVPerson(Person):
    class Meta:
        proxy = True

    objects = models.Manager()
    starts_with_v_objects = StartsWithVManager()
# Proxy model example for a normal model ENDS

