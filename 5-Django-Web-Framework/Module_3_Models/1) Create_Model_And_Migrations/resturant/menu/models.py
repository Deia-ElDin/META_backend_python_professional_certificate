from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=200)
    price = models.IntegerField()
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " : " + self.cuisine + " = " + str(self.price) + " : " + str(self.inventory)