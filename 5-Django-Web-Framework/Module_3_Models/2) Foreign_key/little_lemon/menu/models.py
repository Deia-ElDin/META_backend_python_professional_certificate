from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, default=None, related_name="category_name")


    def __str__(self):
        return "Menu item: " + self.name + " : " + str(self.price) + " : " + str(self.category_id.name)
