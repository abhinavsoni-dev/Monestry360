from django.db import models

# Create your models here.
class booking(models.Model):
    first_name=models.CharField(max_length=122)
    last_name=models.CharField(max_length=122)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    arrival_date=models.DateField()
    arrival_time=models.TimeField()
    departure_date=models.DateField()
    departure_time=models.TimeField()

    def __str__(self):
        return self.name
    


