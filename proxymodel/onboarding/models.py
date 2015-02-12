from django.db import models

# Proxy model example for a custom model
class Person(models.Model):
    class Meta:
        db_table = 'person_info'
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class MyPerson(Person):
    class Meta:
        ordering = ['last_name']
        proxy = True

    def __str__(self):
        return self.first_name

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

# Proxy model example for a normal model ENDS