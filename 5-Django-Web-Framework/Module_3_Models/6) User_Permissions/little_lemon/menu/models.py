from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.name + ": " + str(self.price) + ", inventory:" + str(self.inventory)