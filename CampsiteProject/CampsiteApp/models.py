from django.db import models

# Create your models here.

class BookingRecord(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    arrival_Date = models.DateTimeField()
    depature_Date = models.DateTimeField()
    guests = models.IntegerField()

    class Meta:
        db_table = "booking_record"
        managed = True
    def __str__(self):
        return self.name