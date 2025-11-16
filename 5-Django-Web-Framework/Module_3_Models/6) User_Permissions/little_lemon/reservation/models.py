from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField('Contact Number', max_length=20)
    time = models.TimeField()
    number_of_guests = models.IntegerField()
    notice = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name + ": Reservation" + " for " + str(self.number_of_guests) + " guests"